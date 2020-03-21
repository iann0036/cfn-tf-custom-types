# Terraform::Google::ComputeBackendService

CloudFormation equivalent of google_compute_backend_service

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::ComputeBackendService",
    "Properties" : {
        "<a href="#affinitycookiettlsec" title="AffinityCookieTtlSec">AffinityCookieTtlSec</a>" : <i>Double</i>,
        "<a href="#connectiondrainingtimeoutsec" title="ConnectionDrainingTimeoutSec">ConnectionDrainingTimeoutSec</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#enablecdn" title="EnableCdn">EnableCdn</a>" : <i>Boolean</i>,
        "<a href="#healthchecks" title="HealthChecks">HealthChecks</a>" : <i>[ String, ... ]</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#loadbalancingscheme" title="LoadBalancingScheme">LoadBalancingScheme</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#portname" title="PortName">PortName</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#securitypolicy" title="SecurityPolicy">SecurityPolicy</a>" : <i>String</i>,
        "<a href="#sessionaffinity" title="SessionAffinity">SessionAffinity</a>" : <i>String</i>,
        "<a href="#timeoutsec" title="TimeoutSec">TimeoutSec</a>" : <i>Double</i>,
        "<a href="#backend" title="Backend">Backend</a>" : <i>[ &lt;a href=&#34;backend.md&#34;&gt;Backend&lt;/a&gt;, ... ]</i>,
        "<a href="#cdnpolicy" title="CdnPolicy">CdnPolicy</a>" : <i>[ &lt;a href=&#34;cdnpolicy.md&#34;&gt;CdnPolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#iap" title="Iap">Iap</a>" : <i>[ &lt;a href=&#34;iap.md&#34;&gt;Iap&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#cachekeypolicy" title="CacheKeyPolicy">CacheKeyPolicy</a>" : <i>[ &lt;a href=&#34;cachekeypolicy.md&#34;&gt;CacheKeyPolicy&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::ComputeBackendService
Properties:
    <a href="#affinitycookiettlsec" title="AffinityCookieTtlSec">AffinityCookieTtlSec</a>: <i>Double</i>
    <a href="#connectiondrainingtimeoutsec" title="ConnectionDrainingTimeoutSec">ConnectionDrainingTimeoutSec</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#enablecdn" title="EnableCdn">EnableCdn</a>: <i>Boolean</i>
    <a href="#healthchecks" title="HealthChecks">HealthChecks</a>: <i>
      - String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#loadbalancingscheme" title="LoadBalancingScheme">LoadBalancingScheme</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#portname" title="PortName">PortName</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#securitypolicy" title="SecurityPolicy">SecurityPolicy</a>: <i>String</i>
    <a href="#sessionaffinity" title="SessionAffinity">SessionAffinity</a>: <i>String</i>
    <a href="#timeoutsec" title="TimeoutSec">TimeoutSec</a>: <i>Double</i>
    <a href="#backend" title="Backend">Backend</a>: <i>
      - &lt;a href=&#34;backend.md&#34;&gt;Backend&lt;/a&gt;</i>
    <a href="#cdnpolicy" title="CdnPolicy">CdnPolicy</a>: <i>
      - &lt;a href=&#34;cdnpolicy.md&#34;&gt;CdnPolicy&lt;/a&gt;</i>
    <a href="#iap" title="Iap">Iap</a>: <i>
      - &lt;a href=&#34;iap.md&#34;&gt;Iap&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#cachekeypolicy" title="CacheKeyPolicy">CacheKeyPolicy</a>: <i>
      - &lt;a href=&#34;cachekeypolicy.md&#34;&gt;CacheKeyPolicy&lt;/a&gt;</i>
</pre>

## Properties

#### AffinityCookieTtlSec

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionDrainingTimeoutSec

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableCdn

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthChecks

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancingScheme

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityPolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionAffinity

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeoutSec

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Backend

_Required_: No

_Type_: List of &lt;a href=&#34;backend.md&#34;&gt;Backend&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CdnPolicy

_Required_: No

_Type_: List of &lt;a href=&#34;cdnpolicy.md&#34;&gt;CdnPolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Iap

_Required_: No

_Type_: List of &lt;a href=&#34;iap.md&#34;&gt;Iap&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CacheKeyPolicy

_Required_: No

_Type_: List of &lt;a href=&#34;cachekeypolicy.md&#34;&gt;CacheKeyPolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreationTimestamp

Returns the &lt;code&gt;CreationTimestamp&lt;/code&gt; value.

#### Fingerprint

Returns the &lt;code&gt;Fingerprint&lt;/code&gt; value.

#### SelfLink

Returns the &lt;code&gt;SelfLink&lt;/code&gt; value.

