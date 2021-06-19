# TF::Scaleway::IotRoute

CloudFormation equivalent of scaleway_iot_route

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Scaleway::IotRoute",
    "Properties" : {
        "<a href="#hubid" title="HubId">HubId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#topic" title="Topic">Topic</a>" : <i>String</i>,
        "<a href="#database" title="Database">Database</a>" : <i>[ <a href="databasedefinition.md">DatabaseDefinition</a>, ... ]</i>,
        "<a href="#rest" title="Rest">Rest</a>" : <i>[ <a href="restdefinition.md">RestDefinition</a>, ... ]</i>,
        "<a href="#s3" title="S3">S3</a>" : <i>[ <a href="s3definition.md">S3Definition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Scaleway::IotRoute
Properties:
    <a href="#hubid" title="HubId">HubId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#topic" title="Topic">Topic</a>: <i>String</i>
    <a href="#database" title="Database">Database</a>: <i>
      - <a href="databasedefinition.md">DatabaseDefinition</a></i>
    <a href="#rest" title="Rest">Rest</a>: <i>
      - <a href="restdefinition.md">RestDefinition</a></i>
    <a href="#s3" title="S3">S3</a>: <i>
      - <a href="s3definition.md">S3Definition</a></i>
</pre>

## Properties

#### HubId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Topic

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Database

_Required_: No

_Type_: List of <a href="databasedefinition.md">DatabaseDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rest

_Required_: No

_Type_: List of <a href="restdefinition.md">RestDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3

_Required_: No

_Type_: List of <a href="s3definition.md">S3Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### Id

Returns the <code>Id</code> value.

