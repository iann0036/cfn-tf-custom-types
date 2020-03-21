# Terraform::Fastly::ServiceV1 CacheSetting

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#cachecondition" title="CacheCondition">CacheCondition</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#stalettl" title="StaleTtl">StaleTtl</a>" : <i>Double</i>,
    "<a href="#ttl" title="Ttl">Ttl</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#cachecondition" title="CacheCondition">CacheCondition</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#stalettl" title="StaleTtl">StaleTtl</a>: <i>Double</i>
<a href="#ttl" title="Ttl">Ttl</a>: <i>Double</i>
</pre>

## Properties

#### Action

One of `cache`, `pass`, or `restart`, as defined
on Fastly's documentation under ["Caching action descriptions"](https://docs.fastly.com/guides/performance-tuning/controlling-caching#caching-action-descriptions).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CacheCondition

Name of already defined `condition` used to test whether this settings object should be used. This `condition` must be of type `CACHE`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Unique name for this Cache Setting.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaleTtl

Max "Time To Live" for stale (unreachable) objects.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ttl

The Time-To-Live (TTL) for the object.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

