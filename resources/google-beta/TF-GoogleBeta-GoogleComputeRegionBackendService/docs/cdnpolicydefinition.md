# TF::GoogleBeta::GoogleComputeRegionBackendService CdnPolicyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cachemode" title="CacheMode">CacheMode</a>" : <i>String</i>,
    "<a href="#clientttl" title="ClientTtl">ClientTtl</a>" : <i>Double</i>,
    "<a href="#defaultttl" title="DefaultTtl">DefaultTtl</a>" : <i>Double</i>,
    "<a href="#maxttl" title="MaxTtl">MaxTtl</a>" : <i>Double</i>,
    "<a href="#negativecaching" title="NegativeCaching">NegativeCaching</a>" : <i>Boolean</i>,
    "<a href="#servewhilestale" title="ServeWhileStale">ServeWhileStale</a>" : <i>Double</i>,
    "<a href="#signedurlcachemaxagesec" title="SignedUrlCacheMaxAgeSec">SignedUrlCacheMaxAgeSec</a>" : <i>Double</i>,
    "<a href="#cachekeypolicy" title="CacheKeyPolicy">CacheKeyPolicy</a>" : <i>[ <a href="cachekeypolicydefinition.md">CacheKeyPolicyDefinition</a>, ... ]</i>,
    "<a href="#negativecachingpolicy" title="NegativeCachingPolicy">NegativeCachingPolicy</a>" : <i>[ <a href="negativecachingpolicydefinition.md">NegativeCachingPolicyDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cachemode" title="CacheMode">CacheMode</a>: <i>String</i>
<a href="#clientttl" title="ClientTtl">ClientTtl</a>: <i>Double</i>
<a href="#defaultttl" title="DefaultTtl">DefaultTtl</a>: <i>Double</i>
<a href="#maxttl" title="MaxTtl">MaxTtl</a>: <i>Double</i>
<a href="#negativecaching" title="NegativeCaching">NegativeCaching</a>: <i>Boolean</i>
<a href="#servewhilestale" title="ServeWhileStale">ServeWhileStale</a>: <i>Double</i>
<a href="#signedurlcachemaxagesec" title="SignedUrlCacheMaxAgeSec">SignedUrlCacheMaxAgeSec</a>: <i>Double</i>
<a href="#cachekeypolicy" title="CacheKeyPolicy">CacheKeyPolicy</a>: <i>
      - <a href="cachekeypolicydefinition.md">CacheKeyPolicyDefinition</a></i>
<a href="#negativecachingpolicy" title="NegativeCachingPolicy">NegativeCachingPolicy</a>: <i>
      - <a href="negativecachingpolicydefinition.md">NegativeCachingPolicyDefinition</a></i>
</pre>

## Properties

#### CacheMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientTtl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultTtl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxTtl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NegativeCaching

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServeWhileStale

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SignedUrlCacheMaxAgeSec

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CacheKeyPolicy

_Required_: No

_Type_: List of <a href="cachekeypolicydefinition.md">CacheKeyPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NegativeCachingPolicy

_Required_: No

_Type_: List of <a href="negativecachingpolicydefinition.md">NegativeCachingPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

