# TF::AzureRM::PrivateDnsZone SoaRecordDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#email" title="Email">Email</a>" : <i>String</i>,
    "<a href="#expiretime" title="ExpireTime">ExpireTime</a>" : <i>Double</i>,
    "<a href="#minimumttl" title="MinimumTtl">MinimumTtl</a>" : <i>Double</i>,
    "<a href="#refreshtime" title="RefreshTime">RefreshTime</a>" : <i>Double</i>,
    "<a href="#retrytime" title="RetryTime">RetryTime</a>" : <i>Double</i>,
    "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
    "<a href="#ttl" title="Ttl">Ttl</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#email" title="Email">Email</a>: <i>String</i>
<a href="#expiretime" title="ExpireTime">ExpireTime</a>: <i>Double</i>
<a href="#minimumttl" title="MinimumTtl">MinimumTtl</a>: <i>Double</i>
<a href="#refreshtime" title="RefreshTime">RefreshTime</a>: <i>Double</i>
<a href="#retrytime" title="RetryTime">RetryTime</a>: <i>Double</i>
<a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
<a href="#ttl" title="Ttl">Ttl</a>: <i>Double</i>
</pre>

## Properties

#### Email

The email contact for the SOA record.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpireTime

The expire time for the SOA record. Defaults to `2419200`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinimumTtl

The minimum Time To Live for the SOA record. By convention, it is used to determine the negative caching duration. Defaults to `10`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RefreshTime

The refresh time for the SOA record. Defaults to `3600`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetryTime

The retry time for the SOA record. Defaults to `300`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ttl

The Time To Live of the SOA Record in seconds. Defaults to `3600`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

