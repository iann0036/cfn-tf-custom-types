# TF::GoogleBeta::GoogleComputeBackendService ConsistentHashDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#httpheadername" title="HttpHeaderName">HttpHeaderName</a>" : <i>String</i>,
    "<a href="#minimumringsize" title="MinimumRingSize">MinimumRingSize</a>" : <i>Double</i>,
    "<a href="#httpcookie" title="HttpCookie">HttpCookie</a>" : <i>[ <a href="httpcookiedefinition.md">HttpCookieDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#httpheadername" title="HttpHeaderName">HttpHeaderName</a>: <i>String</i>
<a href="#minimumringsize" title="MinimumRingSize">MinimumRingSize</a>: <i>Double</i>
<a href="#httpcookie" title="HttpCookie">HttpCookie</a>: <i>
      - <a href="httpcookiedefinition.md">HttpCookieDefinition</a></i>
</pre>

## Properties

#### HttpHeaderName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinimumRingSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpCookie

_Required_: No

_Type_: List of <a href="httpcookiedefinition.md">HttpCookieDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

