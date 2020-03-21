# Terraform::AzureRM::BatchPool EndpointConfiguration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#backendport" title="BackendPort">BackendPort</a>" : <i>Double</i>,
    "<a href="#frontendportrange" title="FrontendPortRange">FrontendPortRange</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
    "<a href="#networksecuritygrouprules" title="NetworkSecurityGroupRules">NetworkSecurityGroupRules</a>" : <i>[ <a href="endpointconfiguration-networksecuritygrouprules.md">NetworkSecurityGroupRules</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#backendport" title="BackendPort">BackendPort</a>: <i>Double</i>
<a href="#frontendportrange" title="FrontendPortRange">FrontendPortRange</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
<a href="#networksecuritygrouprules" title="NetworkSecurityGroupRules">NetworkSecurityGroupRules</a>: <i>
      - <a href="endpointconfiguration-networksecuritygrouprules.md">NetworkSecurityGroupRules</a></i>
</pre>

## Properties

#### BackendPort

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FrontendPortRange

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkSecurityGroupRules

_Required_: No
_Type_: List of <a href="endpointconfiguration-networksecuritygrouprules.md">NetworkSecurityGroupRules</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

