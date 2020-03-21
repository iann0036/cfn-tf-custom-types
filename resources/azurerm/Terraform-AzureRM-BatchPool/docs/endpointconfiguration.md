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

The port number on the compute node. Acceptable values are between `1` and `65535` except for `29876`, `29877` as these are reserved. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FrontendPortRange

The range of external ports that will be used to provide inbound access to the backendPort on individual compute nodes in the format of `1000-1100`. Acceptable values range between `1` and `65534` except ports from `50000` to `55000` which are reserved by the Batch service. All ranges within a pool must be distinct and cannot overlap. Values must be a range of at least `100` nodes. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the endpoint. The name must be unique within a Batch pool, can contain letters, numbers, underscores, periods, and hyphens. Names must start with a letter or number, must end with a letter, number, or underscore, and cannot exceed 77 characters. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

The protocol of the endpoint. Acceptable values are `TCP` and `UDP`. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkSecurityGroupRules

_Required_: No

_Type_: List of <a href="endpointconfiguration-networksecuritygrouprules.md">NetworkSecurityGroupRules</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

