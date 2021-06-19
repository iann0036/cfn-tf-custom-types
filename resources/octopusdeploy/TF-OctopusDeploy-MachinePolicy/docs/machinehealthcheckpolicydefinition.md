# TF::OctopusDeploy::MachinePolicy MachineHealthCheckPolicyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#healthcheckcron" title="HealthCheckCron">HealthCheckCron</a>" : <i>String</i>,
    "<a href="#healthcheckcrontimezone" title="HealthCheckCronTimezone">HealthCheckCronTimezone</a>" : <i>String</i>,
    "<a href="#healthcheckinterval" title="HealthCheckInterval">HealthCheckInterval</a>" : <i>Double</i>,
    "<a href="#healthchecktype" title="HealthCheckType">HealthCheckType</a>" : <i>String</i>,
    "<a href="#bashhealthcheckpolicy" title="BashHealthCheckPolicy">BashHealthCheckPolicy</a>" : <i>[ <a href="bashhealthcheckpolicydefinition.md">BashHealthCheckPolicyDefinition</a>, ... ]</i>,
    "<a href="#powershellhealthcheckpolicy" title="PowershellHealthCheckPolicy">PowershellHealthCheckPolicy</a>" : <i>[ <a href="powershellhealthcheckpolicydefinition.md">PowershellHealthCheckPolicyDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#healthcheckcron" title="HealthCheckCron">HealthCheckCron</a>: <i>String</i>
<a href="#healthcheckcrontimezone" title="HealthCheckCronTimezone">HealthCheckCronTimezone</a>: <i>String</i>
<a href="#healthcheckinterval" title="HealthCheckInterval">HealthCheckInterval</a>: <i>Double</i>
<a href="#healthchecktype" title="HealthCheckType">HealthCheckType</a>: <i>String</i>
<a href="#bashhealthcheckpolicy" title="BashHealthCheckPolicy">BashHealthCheckPolicy</a>: <i>
      - <a href="bashhealthcheckpolicydefinition.md">BashHealthCheckPolicyDefinition</a></i>
<a href="#powershellhealthcheckpolicy" title="PowershellHealthCheckPolicy">PowershellHealthCheckPolicy</a>: <i>
      - <a href="powershellhealthcheckpolicydefinition.md">PowershellHealthCheckPolicyDefinition</a></i>
</pre>

## Properties

#### HealthCheckCron

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckCronTimezone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BashHealthCheckPolicy

_Required_: No

_Type_: List of <a href="bashhealthcheckpolicydefinition.md">BashHealthCheckPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PowershellHealthCheckPolicy

_Required_: No

_Type_: List of <a href="powershellhealthcheckpolicydefinition.md">PowershellHealthCheckPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

