# Terraform::Rancher::RegistrationToken

Provides a Rancher Registration Token resource. This can be used to create registration tokens for rancher environments and retrieve their information.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Rancher::RegistrationToken",
    "Properties" : {
        "<a href="#agentip" title="AgentIp">AgentIp</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#environmentid" title="EnvironmentId">EnvironmentId</a>" : <i>String</i>,
        "<a href="#hostlabels" title="HostLabels">HostLabels</a>" : <i>[ <a href="hostlabels.md">HostLabels</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Rancher::RegistrationToken
Properties:
    <a href="#agentip" title="AgentIp">AgentIp</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#environmentid" title="EnvironmentId">EnvironmentId</a>: <i>String</i>
    <a href="#hostlabels" title="HostLabels">HostLabels</a>: <i>
      - <a href="hostlabels.md">HostLabels</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
</pre>

## Properties

#### AgentIp

A string containing the CATTLE_AGENT_IP to add to the registration command.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A registration token description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnvironmentId

The ID of the environment to create the token for.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostLabels

A map of host labels to add to the registration command.

_Required_: No

_Type_: List of <a href="hostlabels.md">HostLabels</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the registration token.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Command

Returns the <code>Command</code> value.

#### Id

Returns the <code>Id</code> value.

#### Image

Returns the <code>Image</code> value.

#### RegistrationUrl

Returns the <code>RegistrationUrl</code> value.

#### Token

Returns the <code>Token</code> value.

