# guardrails.py
from pydantic import BaseModel
from agents import Agent, GuardrailFunctionOutput, Runner, input_guardrail

class PIIOutput(BaseModel):
    has_pii: bool
    reason:  str

PII_GUARDRAIL_AGENT = Agent(
    name="PII Guardrail Agent",
    instructions="""
      Detect if the input has any PII (address, SSN, credit card, bank account, etc.).
      Return JSON exactly as:
        {"has_pii": <true|false>, "reason": "<explanation>"}
    """,
    output_type=PIIOutput
)

@input_guardrail  # <-- decorate it!
async def pii_guardrail(ctx, agent, user_input: str):
    result    = await Runner.run(PII_GUARDRAIL_AGENT, user_input, context=ctx.context)
    guard_out = result.final_output_as(PIIOutput)
    return GuardrailFunctionOutput(
        output_info=guard_out,
        tripwire_triggered=guard_out.has_pii
    )