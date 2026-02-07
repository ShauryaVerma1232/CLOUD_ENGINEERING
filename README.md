# CLOUD_ENGINEERING
Day 1 — Cloud Engineering Foundations
Repository: CLOUD_ENGINEERING
System Purpose
"The goal of this lab is to build a minimal, intentionally exposed cloud system to practice operability, observability, and failure analysis, not application development".

This system is designed to:
Expose a workload to the internet in a controlled way
Generate realistic operational signals
Serve as a baseline for detection, response, and scaling decisions
This is not a production system. It is a learning surface.
Architecture Overview

Cloud Provider: Azure
Region: West US 3
Compute: Single Ubuntu Linux VM (D-series)

Networking:
Virtual Network with a single subnet
Network Security Group (NSG) applied at subnet level
Public IP attached to the VM

Access:
SSH restricted to a single admin IP
Port 8080 intentionally open to the internet

Observability:
Azure Activity Logs (control plane)
Boot Diagnostics (recovery plane)
NSG Flow Logs (data plane)

Design Decisions
1. Single VM, No Redundancy
Chosen deliberately to:
Surface single points of failure
Force manual investigation
Avoid hiding problems behind managed services

2. Public IP + Open Port (8080)
The system is intentionally exposed to:
Observe unsolicited traffic
Practice threat modeling
Generate noisy but realistic network logs
This exposure is a learning tool, not a mistake.

3. NSG at Subnet Level
Applying the NSG at the subnet:
Simplifies rule management
Mirrors common early-stage architectures
Makes blast radius explicit

4. Compute Is Ephemeral
The VM is stopped and deallocated when not in use:
Cost is controlled
State is preserved
Reinforces cloud-native thinking: compute is temporary
Exposure by Design
This system is exposed in the following ways:
Public IP reachable from the internet
Port 8080 open to 0.0.0.0/0
No rate limiting or application firewall
No DDoS protection enabled
This exposure is intentional to:
Study traffic patterns
Observe failure modes
Practice detection logic later
Failure Modes (Observed & Expected)

If Traffic Spikes:
VM CPU saturates before Azure reports an error
SSH responsiveness degrades
Legitimate and malicious traffic compete equally

What Breaks First:
VM performance, not availability
Operator visibility, not the system itself

Silent Failures:
The system may appear “up” while being unusable
No automatic alerting triggers by default

Observability Gaps:
Current limitations identified on Day 1:
No CPU or memory alerts
No application-level logging
No rate-of-change detection
No baseline for “normal” traffic
No correlation between NSG logs and VM health

The system answers:
“Did something happen?”

It does not yet answer:
“Is this abnormal, dangerous, or expected?”

Day 1 Detection Work
A simple Python script was built to:
Read event-style inputs
Count repeated actions
Apply a threshold
Flag suspicious repetition

This models:
Abuse detection
Rate limiting logic
Alerting primitives
The script is intentionally simple and mirrors real-world detection patterns at a conceptual level.
Next Improvements (Planned)

Priority order moving forward:
Add resource-level metrics (CPU, network)
Define alert thresholds and notifications
Introduce time windows into detection logic
Correlate network logs with host state
Separate exposure layer from compute
Introduce scaling or buffering mechanisms
Key Takeaway — Day 1
This lab is successful because it is incomplete by design.

It reveals:
Where systems fail quietly
Where visibility is missing  
Why “it works” is not the same as “it’s operable”
This is the foundation for moving from cloud usage to cloud engineering. 
