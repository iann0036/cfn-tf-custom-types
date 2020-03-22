# Terraform::Alicloud::PolardbAccountPrivilege

Provides a PolarDB account privilege resource and used to grant several database some access privilege. A database can be granted by multiple account.

-> **NOTE:** Available in v1.67.0+.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::PolardbAccountPrivilege",
    "Properties" : {
        "<a href="#accountname" title="AccountName">AccountName</a>" : <i>String</i>,
        "<a href="#accountprivilege" title="AccountPrivilege">AccountPrivilege</a>" : <i>String</i>,
        "<a href="#dbclusterid" title="DbClusterId">DbClusterId</a>" : <i>String</i>,
        "<a href="#dbnames" title="DbNames">DbNames</a>" : <i>[ String, ... ]</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::PolardbAccountPrivilege
Properties:
    <a href="#accountname" title="AccountName">AccountName</a>: <i>String</i>
    <a href="#accountprivilege" title="AccountPrivilege">AccountPrivilege</a>: <i>String</i>
    <a href="#dbclusterid" title="DbClusterId">DbClusterId</a>: <i>String</i>
    <a href="#dbnames" title="DbNames">DbNames</a>: <i>
      - String</i>
</pre>

## Properties

#### AccountName

A specified account name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountPrivilege

The privilege of one account access database. Valid values: ["ReadOnly", "ReadWrite"]. Default to "ReadOnly".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbClusterId

The Id of cluster in which account belongs.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbNames

List of specified database name.

_Required_: Yes

_Type_: List of String

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

