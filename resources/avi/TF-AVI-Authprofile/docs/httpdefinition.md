# TF::AVI::Authprofile HttpDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cacheexpirationtime" title="CacheExpirationTime">CacheExpirationTime</a>" : <i>Double</i>,
    "<a href="#requestheader" title="RequestHeader">RequestHeader</a>" : <i>String</i>,
    "<a href="#requireusergroups" title="RequireUserGroups">RequireUserGroups</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cacheexpirationtime" title="CacheExpirationTime">CacheExpirationTime</a>: <i>Double</i>
<a href="#requestheader" title="RequestHeader">RequestHeader</a>: <i>String</i>
<a href="#requireusergroups" title="RequireUserGroups">RequireUserGroups</a>: <i>
      - String</i>
</pre>

## Properties

#### CacheExpirationTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestHeader

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequireUserGroups

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

