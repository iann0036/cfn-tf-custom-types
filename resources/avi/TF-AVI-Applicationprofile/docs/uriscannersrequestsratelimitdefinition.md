# TF::AVI::Applicationprofile UriScannersRequestsRateLimitDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#explicittracking" title="ExplicitTracking">ExplicitTracking</a>" : <i>Boolean</i>,
    "<a href="#finegrain" title="FineGrain">FineGrain</a>" : <i>Boolean</i>,
    "<a href="#httpcookie" title="HttpCookie">HttpCookie</a>" : <i>String</i>,
    "<a href="#httpheader" title="HttpHeader">HttpHeader</a>" : <i>String</i>,
    "<a href="#action" title="Action">Action</a>" : <i>[ <a href="actiondefinition.md">ActionDefinition</a>, ... ]</i>,
    "<a href="#ratelimiter" title="RateLimiter">RateLimiter</a>" : <i>[ <a href="ratelimiterdefinition.md">RateLimiterDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#explicittracking" title="ExplicitTracking">ExplicitTracking</a>: <i>Boolean</i>
<a href="#finegrain" title="FineGrain">FineGrain</a>: <i>Boolean</i>
<a href="#httpcookie" title="HttpCookie">HttpCookie</a>: <i>String</i>
<a href="#httpheader" title="HttpHeader">HttpHeader</a>: <i>String</i>
<a href="#action" title="Action">Action</a>: <i>
      - <a href="actiondefinition.md">ActionDefinition</a></i>
<a href="#ratelimiter" title="RateLimiter">RateLimiter</a>: <i>
      - <a href="ratelimiterdefinition.md">RateLimiterDefinition</a></i>
</pre>

## Properties

#### ExplicitTracking

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FineGrain

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpCookie

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpHeader

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Action

_Required_: No

_Type_: List of <a href="actiondefinition.md">ActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RateLimiter

_Required_: No

_Type_: List of <a href="ratelimiterdefinition.md">RateLimiterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

