# Terraform::AWS::GlueConnection

CloudFormation equivalent of aws_glue_connection

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::GlueConnection",
    "Properties" : {
        "<a href="#catalogid" title="CatalogId">CatalogId</a>" : <i>String</i>,
        "<a href="#connectionproperties" title="ConnectionProperties">ConnectionProperties</a>" : <i>[ <a href="connectionproperties.md">ConnectionProperties</a>, ... ]</i>,
        "<a href="#connectiontype" title="ConnectionType">ConnectionType</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#matchcriteria" title="MatchCriteria">MatchCriteria</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#physicalconnectionrequirements" title="PhysicalConnectionRequirements">PhysicalConnectionRequirements</a>" : <i>[ <a href="physicalconnectionrequirements.md">PhysicalConnectionRequirements</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::GlueConnection
Properties:
    <a href="#catalogid" title="CatalogId">CatalogId</a>: <i>String</i>
    <a href="#connectionproperties" title="ConnectionProperties">ConnectionProperties</a>: <i>
      - <a href="connectionproperties.md">ConnectionProperties</a></i>
    <a href="#connectiontype" title="ConnectionType">ConnectionType</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#matchcriteria" title="MatchCriteria">MatchCriteria</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#physicalconnectionrequirements" title="PhysicalConnectionRequirements">PhysicalConnectionRequirements</a>: <i>
      - <a href="physicalconnectionrequirements.md">PhysicalConnectionRequirements</a></i>
</pre>

## Properties

#### CatalogId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionProperties

_Required_: Yes

_Type_: List of <a href="connectionproperties.md">ConnectionProperties</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchCriteria

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PhysicalConnectionRequirements

_Required_: No

_Type_: List of <a href="physicalconnectionrequirements.md">PhysicalConnectionRequirements</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

