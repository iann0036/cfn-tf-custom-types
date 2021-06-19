# TF::Alicloud::AdbConnection

Provides an ADB connection resource to allocate an Internet connection string for ADB cluster.

-> **NOTE:** Each ADB instance will allocate a intranet connnection string automatically and its prifix is ADB instance ID.
 To avoid unnecessary conflict, please specified a internet connection prefix before applying the resource.

-> **NOTE:** Available in v1.81.0+.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::AdbConnection",
    "Properties" : {
        "<a href="#connectionprefix" title="ConnectionPrefix">ConnectionPrefix</a>" : <i>String</i>,
        "<a href="#dbclusterid" title="DbClusterId">DbClusterId</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::AdbConnection
Properties:
    <a href="#connectionprefix" title="ConnectionPrefix">ConnectionPrefix</a>: <i>String</i>
    <a href="#dbclusterid" title="DbClusterId">DbClusterId</a>: <i>String</i>
</pre>

## Properties

#### ConnectionPrefix

Prefix of an Internet connection string. It must be checked for uniqueness. It may consist of lowercase letters, numbers, and underlines, and must start with a letter and have no more than 30 characters. Default to <db_cluster_id> + 'tf'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbClusterId

The Id of cluster that can run database.

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

#### ConnectionString

Returns the <code>ConnectionString</code> value.

#### Id

Returns the <code>Id</code> value.

#### IpAddress

Returns the <code>IpAddress</code> value.

#### Port

Returns the <code>Port</code> value.

