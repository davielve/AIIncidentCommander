# General Incident Response Triaging

## Objective
To identify the root cause of a service degradation and propose immediate mitigation steps.

## Steps
1. **Analyze Logs**: Look for ERROR or FATAL levels in the last 5 minutes.
2. **Check Health**: Verify if the service health score is below 80%.
3. **Correlate**: Check if database errors correlate with application timeouts.
4. **Classify Severity**:
   - **Critical**: Service is down or data loss is occurring.
   - **Warning**: Service is slow but functional.
   - **Info**: Normal operations or minor anomalies.

## Remediation Policy
- Always require human approval for restarts.
- Rollbacks should only be suggested if a recent deployment occurred.
