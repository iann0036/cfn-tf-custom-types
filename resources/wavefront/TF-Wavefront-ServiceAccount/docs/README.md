# TF::Wavefront::ServiceAccount

CloudFormation equivalent of wavefront_service_account

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Wavefront::ServiceAccount",
    "Properties" : {
        "<a href="#active" title="Active">Active</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#identifier" title="Identifier">Identifier</a>" : <i>String</i>,
        "<a href="#ingestionpolicy" title="IngestionPolicy">IngestionPolicy</a>" : <i>String</i>,
        "<a href="#permissions" title="Permissions">Permissions</a>" : <i>[ String, ... ]</i>,
        "<a href="#usergroups" title="UserGroups">UserGroups</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Wavefront::ServiceAccount
Properties:
    <a href="#active" title="Active">Active</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#identifier" title="Identifier">Identifier</a>: <i>String</i>
    <a href="#ingestionpolicy" title="IngestionPolicy">IngestionPolicy</a>: <i>String</i>
    <a href="#permissions" title="Permissions">Permissions</a>: <i>
      - String</i>
    <a href="#usergroups" title="UserGroups">UserGroups</a>: <i>
      - String</i>
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

#### Identifier

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IngestionPolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Permissions

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserGroups

_Required_: No

_Type_: List of String

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

