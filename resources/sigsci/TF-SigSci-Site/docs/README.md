# TF::SigSci::Site

CloudFormation equivalent of sigsci_site

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::SigSci::Site",
    "Properties" : {
        "<a href="#agentanonmode" title="AgentAnonMode">AgentAnonMode</a>" : <i>String</i>,
        "<a href="#agentlevel" title="AgentLevel">AgentLevel</a>" : <i>String</i>,
        "<a href="#blockdurationseconds" title="BlockDurationSeconds">BlockDurationSeconds</a>" : <i>Double</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#shortname" title="ShortName">ShortName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::SigSci::Site
Properties:
    <a href="#agentanonmode" title="AgentAnonMode">AgentAnonMode</a>: <i>String</i>
    <a href="#agentlevel" title="AgentLevel">AgentLevel</a>: <i>String</i>
    <a href="#blockdurationseconds" title="BlockDurationSeconds">BlockDurationSeconds</a>: <i>Double</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#shortname" title="ShortName">ShortName</a>: <i>String</i>
</pre>

## Properties

#### AgentAnonMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AgentLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockDurationSeconds

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShortName

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

#### BlockHttpCode

Returns the <code>BlockHttpCode</code> value.

#### Id

Returns the <code>Id</code> value.

#### PrimaryAgentKey

Returns the <code>PrimaryAgentKey</code> value.

