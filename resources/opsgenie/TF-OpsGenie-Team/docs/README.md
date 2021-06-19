# TF::OpsGenie::Team

Manages a Team within Opsgenie.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OpsGenie::Team",
    "Properties" : {
        "<a href="#deletedefaultresources" title="DeleteDefaultResources">DeleteDefaultResources</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#ignoremembers" title="IgnoreMembers">IgnoreMembers</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#member" title="Member">Member</a>" : <i>[ <a href="memberdefinition.md">MemberDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OpsGenie::Team
Properties:
    <a href="#deletedefaultresources" title="DeleteDefaultResources">DeleteDefaultResources</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#ignoremembers" title="IgnoreMembers">IgnoreMembers</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#member" title="Member">Member</a>: <i>
      - <a href="memberdefinition.md">MemberDefinition</a></i>
</pre>

## Properties

#### DeleteDefaultResources

Set to true to remove default escalation and schedule for newly created team. **Be careful its also changes that team routing rule to None. That means you have to define routing rule as well**.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A description for this team.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreMembers

Set to true to ignore any configured member blocks and any team member added/updated/removed via OpsGenie web UI. Use this option e.g. to maintain membership via web UI only and use it only for new teams. Changing the value for existing teams might lead to strange behaviour. Default: `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name associated with this team. Opsgenie defines that this must not be longer than 100 characters.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Member

_Required_: No

_Type_: List of <a href="memberdefinition.md">MemberDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

