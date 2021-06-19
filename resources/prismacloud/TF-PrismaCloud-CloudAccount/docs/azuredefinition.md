# TF::PrismaCloud::CloudAccount AzureDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#accountid" title="AccountId">AccountId</a>" : <i>String</i>,
    "<a href="#accounttype" title="AccountType">AccountType</a>" : <i>String</i>,
    "<a href="#clientid" title="ClientId">ClientId</a>" : <i>String</i>,
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#groupids" title="GroupIds">GroupIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#key" title="Key">Key</a>" : <i>String</i>,
    "<a href="#monitorflowlogs" title="MonitorFlowLogs">MonitorFlowLogs</a>" : <i>Boolean</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#protectionmode" title="ProtectionMode">ProtectionMode</a>" : <i>String</i>,
    "<a href="#serviceprincipalid" title="ServicePrincipalId">ServicePrincipalId</a>" : <i>String</i>,
    "<a href="#tenantid" title="TenantId">TenantId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#accountid" title="AccountId">AccountId</a>: <i>String</i>
<a href="#accounttype" title="AccountType">AccountType</a>: <i>String</i>
<a href="#clientid" title="ClientId">ClientId</a>: <i>String</i>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#groupids" title="GroupIds">GroupIds</a>: <i>
      - String</i>
<a href="#key" title="Key">Key</a>: <i>String</i>
<a href="#monitorflowlogs" title="MonitorFlowLogs">MonitorFlowLogs</a>: <i>Boolean</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#protectionmode" title="ProtectionMode">ProtectionMode</a>: <i>String</i>
<a href="#serviceprincipalid" title="ServicePrincipalId">ServicePrincipalId</a>: <i>String</i>
<a href="#tenantid" title="TenantId">TenantId</a>: <i>String</i>
</pre>

## Properties

#### AccountId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupIds

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Key

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MonitorFlowLogs

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtectionMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServicePrincipalId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

