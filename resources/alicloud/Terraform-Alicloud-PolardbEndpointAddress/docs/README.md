# Terraform::Alicloud::PolardbEndpointAddress

Provides a PolarDB endpoint address resource to allocate an Internet endpoint address string for PolarDB instance.

-> **NOTE:** Available in v1.68.0+. Each PolarDB instance will allocate a intranet connection string automatically and its prefix is Cluster ID.
 To avoid unnecessary conflict, please specified a internet connection prefix before applying the resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::PolardbEndpointAddress",
    "Properties" : {
        "<a href="#connectionprefix" title="ConnectionPrefix">ConnectionPrefix</a>" : <i>String</i>,
        "<a href="#dbclusterid" title="DbClusterId">DbClusterId</a>" : <i>String</i>,
        "<a href="#dbendpointid" title="DbEndpointId">DbEndpointId</a>" : <i>String</i>,
        "<a href="#nettype" title="NetType">NetType</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::PolardbEndpointAddress
Properties:
    <a href="#connectionprefix" title="ConnectionPrefix">ConnectionPrefix</a>: <i>String</i>
    <a href="#dbclusterid" title="DbClusterId">DbClusterId</a>: <i>String</i>
    <a href="#dbendpointid" title="DbEndpointId">DbEndpointId</a>: <i>String</i>
    <a href="#nettype" title="NetType">NetType</a>: <i>String</i>
</pre>

## Properties

#### ConnectionPrefix

Prefix of an Internet connection string. It must be checked for uniqueness. It may consist of lowercase letters, numbers, and underlines, and must start with a letter and have no more than 30 characters. Default to <db_endpoint_id> + 'tf'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbClusterId

The Id of cluster that can run database.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbEndpointId

The Id of endpoint that can run database.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetType

Internet connection net type. Valid value: `Public`. Default to `Public`. Currently supported only `Public`.

_Required_: No

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

#### ConnectionString

Returns the <code>ConnectionString</code> value.

#### IpAddress

Returns the <code>IpAddress</code> value.

#### Port

Returns the <code>Port</code> value.

