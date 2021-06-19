# TF::Lacework::AgentAccessToken

To connect to the Lacework platform, Lacework agents require an agent access token. Use this resource to
manage agent tokens within your Lacework account. 

!> **Warning:** Agent tokens should be treated as secret and not published. A token uniquely identifies
a Lacework customer. If you suspect your token has been publicly exposed or compromised, generate a new
token, update the new token on all machines using the old token. When complete, the old token can safely
be disabled without interrupting Lacework services.

You can use the agent token name to logically separate your deployments, for example, by environment types
(QA, Dev, etc.) or system types (CentOS, RHEL, etc.).

-> **Note:** The Lacework agent runs on most Linux distributions. For more detailed information, see
	[Supported Operating Systems.](https://support.lacework.com/hc/en-us/articles/360005230014-Supported-Operating-Systems).

!> **Warning:** By design, agent tokens cannot be deleted. Running terraform destroy will only disable the token.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Lacework::AgentAccessToken",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Lacework::AgentAccessToken
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
</pre>

## Properties

#### Description

The agent access token description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The agent access token name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Account

Returns the <code>Account</code> value.

#### CreatedTime

Returns the <code>CreatedTime</code> value.

#### Id

Returns the <code>Id</code> value.

#### LastUpdatedTime

Returns the <code>LastUpdatedTime</code> value.

#### Token

Returns the <code>Token</code> value.

#### Version

Returns the <code>Version</code> value.

