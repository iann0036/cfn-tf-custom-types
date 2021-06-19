# TF::MongoDBAtlas::PrivateIpMode

`mongodbatlas_private_ip_mode` provides a Private IP Mode resource. This allows one to disable Connect via Peering Only mode for a MongoDB Atlas Project.

~> **Deprecated Feature**: <br> This feature has been deprecated. Use [Split Horizon connection strings](https://dochub.mongodb.org/core/atlas-horizon-faq) to connect to your cluster. These connection strings allow you to connect using both VPC/VNet Peering and whitelisted public IP addresses. To learn more about support for Split Horizon, see [this FAQ](https://dochub.mongodb.org/core/atlas-horizon-faq). You need this endpoint to [disable Peering Only](https://docs.atlas.mongodb.com/reference/faq/connection-changes/#disable-peering-mode).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::MongoDBAtlas::PrivateIpMode",
    "Properties" : {
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::MongoDBAtlas::PrivateIpMode
Properties:
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
</pre>

## Properties

#### Enabled

Indicates whether Connect via Peering Only mode is enabled or disabled for an Atlas project.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

The unique ID for the project to enable Only Private IP Mode.

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

#### Id

Returns the <code>Id</code> value.

