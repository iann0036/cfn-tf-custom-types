# TF::GoogleBeta::GoogleStorageObjectAcl

CloudFormation equivalent of google_storage_object_acl

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::GoogleBeta::GoogleStorageObjectAcl",
    "Properties" : {
        "<a href="#bucket" title="Bucket">Bucket</a>" : <i>String</i>,
        "<a href="#object" title="Object">Object</a>" : <i>String</i>,
        "<a href="#predefinedacl" title="PredefinedAcl">PredefinedAcl</a>" : <i>String</i>,
        "<a href="#roleentity" title="RoleEntity">RoleEntity</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::GoogleBeta::GoogleStorageObjectAcl
Properties:
    <a href="#bucket" title="Bucket">Bucket</a>: <i>String</i>
    <a href="#object" title="Object">Object</a>: <i>String</i>
    <a href="#predefinedacl" title="PredefinedAcl">PredefinedAcl</a>: <i>String</i>
    <a href="#roleentity" title="RoleEntity">RoleEntity</a>: <i>
      - String</i>
</pre>

## Properties

#### Bucket

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Object

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PredefinedAcl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleEntity

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

