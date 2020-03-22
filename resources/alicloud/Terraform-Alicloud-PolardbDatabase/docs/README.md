# Terraform::Alicloud::PolardbDatabase

CloudFormation equivalent of alicloud_polardb_database

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::PolardbDatabase",
    "Properties" : {
        "<a href="#charactersetname" title="CharacterSetName">CharacterSetName</a>" : <i>String</i>,
        "<a href="#dbclusterid" title="DbClusterId">DbClusterId</a>" : <i>String</i>,
        "<a href="#dbdescription" title="DbDescription">DbDescription</a>" : <i>String</i>,
        "<a href="#dbname" title="DbName">DbName</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::PolardbDatabase
Properties:
    <a href="#charactersetname" title="CharacterSetName">CharacterSetName</a>: <i>String</i>
    <a href="#dbclusterid" title="DbClusterId">DbClusterId</a>: <i>String</i>
    <a href="#dbdescription" title="DbDescription">DbDescription</a>: <i>String</i>
    <a href="#dbname" title="DbName">DbName</a>: <i>String</i>
</pre>

## Properties

#### CharacterSetName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbClusterId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbDescription

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbName

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

#### Id

Returns the <code>Id</code> value.

