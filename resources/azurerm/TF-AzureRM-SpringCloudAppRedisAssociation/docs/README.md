# TF::AzureRM::SpringCloudAppRedisAssociation

Associates a [Spring Cloud Application](spring_cloud_app.html) with a [Redis Cache](redis_cache.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::SpringCloudAppRedisAssociation",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#redisaccesskey" title="RedisAccessKey">RedisAccessKey</a>" : <i>String</i>,
        "<a href="#rediscacheid" title="RedisCacheId">RedisCacheId</a>" : <i>String</i>,
        "<a href="#springcloudappid" title="SpringCloudAppId">SpringCloudAppId</a>" : <i>String</i>,
        "<a href="#sslenabled" title="SslEnabled">SslEnabled</a>" : <i>Boolean</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::SpringCloudAppRedisAssociation
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#redisaccesskey" title="RedisAccessKey">RedisAccessKey</a>: <i>String</i>
    <a href="#rediscacheid" title="RedisCacheId">RedisCacheId</a>: <i>String</i>
    <a href="#springcloudappid" title="SpringCloudAppId">SpringCloudAppId</a>: <i>String</i>
    <a href="#sslenabled" title="SslEnabled">SslEnabled</a>: <i>Boolean</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Name

Specifies the name of the Spring Cloud Application Association. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedisAccessKey

Specifies the Redis Cache access key.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedisCacheId

Specifies the Redis Cache resource ID. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpringCloudAppId

Specifies the Spring Cloud Application resource ID in which the Association is created. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslEnabled

Should SSL be used when connecting to Redis? Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

