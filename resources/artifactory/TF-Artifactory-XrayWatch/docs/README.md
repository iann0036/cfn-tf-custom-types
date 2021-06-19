# TF::Artifactory::XrayWatch

CloudFormation equivalent of artifactory_xray_watch

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Artifactory::XrayWatch",
    "Properties" : {
        "<a href="#active" title="Active">Active</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#watchrecipients" title="WatchRecipients">WatchRecipients</a>" : <i>[ String, ... ]</i>,
        "<a href="#assignedpolicies" title="AssignedPolicies">AssignedPolicies</a>" : <i>[ <a href="assignedpoliciesdefinition.md">AssignedPoliciesDefinition</a>, ... ]</i>,
        "<a href="#resources" title="Resources">Resources</a>" : <i>[ <a href="resourcesdefinition.md">ResourcesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Artifactory::XrayWatch
Properties:
    <a href="#active" title="Active">Active</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#watchrecipients" title="WatchRecipients">WatchRecipients</a>: <i>
      - String</i>
    <a href="#assignedpolicies" title="AssignedPolicies">AssignedPolicies</a>: <i>
      - <a href="assignedpoliciesdefinition.md">AssignedPoliciesDefinition</a></i>
    <a href="#resources" title="Resources">Resources</a>: <i>
      - <a href="resourcesdefinition.md">ResourcesDefinition</a></i>
</pre>

## Properties

#### Active

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WatchRecipients

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AssignedPolicies

_Required_: No

_Type_: List of <a href="assignedpoliciesdefinition.md">AssignedPoliciesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Resources

_Required_: No

_Type_: List of <a href="resourcesdefinition.md">ResourcesDefinition</a>

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

