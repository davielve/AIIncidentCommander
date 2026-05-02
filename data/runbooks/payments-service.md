# Payments Service Troubleshooting

## Known Issues
### Upstream Timeout
- **Symptom**: "Connection timeout to upstream payment provider" in logs.
- **Cause**: The external payment gateway is slow or down.
- **Action**: Check external status page. Do NOT restart the service, as it won't help. Suggest increasing timeout or switching to backup provider (simulated).

### Database Pool Exhaustion
- **Symptom**: "DB connection pool exhaustion" in logs.
- **Cause**: High traffic or leaking connections.
- **Action**: Suggest a restart of the service to clear the pool.
