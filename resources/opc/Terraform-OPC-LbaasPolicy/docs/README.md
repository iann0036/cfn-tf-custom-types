# Terraform::OPC::LbaasPolicy

CloudFormation equivalent of opc_lbaas_policy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OPC::LbaasPolicy",
    "Properties" : {
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#loadbalancer" title="LoadBalancer">LoadBalancer</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#applicationcookiestickinesspolicy" title="ApplicationCookieStickinessPolicy">ApplicationCookieStickinessPolicy</a>" : <i>[ &lt;a href=&#34;applicationcookiestickinesspolicy.md&#34;&gt;ApplicationCookieStickinessPolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#cloudgatepolicy" title="CloudgatePolicy">CloudgatePolicy</a>" : <i>[ &lt;a href=&#34;cloudgatepolicy.md&#34;&gt;CloudgatePolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#loadbalancercookiestickinesspolicy" title="LoadBalancerCookieStickinessPolicy">LoadBalancerCookieStickinessPolicy</a>" : <i>[ &lt;a href=&#34;loadbalancercookiestickinesspolicy.md&#34;&gt;LoadBalancerCookieStickinessPolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#loadbalancingmechanismpolicy" title="LoadBalancingMechanismPolicy">LoadBalancingMechanismPolicy</a>" : <i>[ &lt;a href=&#34;loadbalancingmechanismpolicy.md&#34;&gt;LoadBalancingMechanismPolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#ratelimitingrequestpolicy" title="RateLimitingRequestPolicy">RateLimitingRequestPolicy</a>" : <i>[ &lt;a href=&#34;ratelimitingrequestpolicy.md&#34;&gt;RateLimitingRequestPolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#redirectpolicy" title="RedirectPolicy">RedirectPolicy</a>" : <i>[ &lt;a href=&#34;redirectpolicy.md&#34;&gt;RedirectPolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#resourceaccesscontrolpolicy" title="ResourceAccessControlPolicy">ResourceAccessControlPolicy</a>" : <i>[ &lt;a href=&#34;resourceaccesscontrolpolicy.md&#34;&gt;ResourceAccessControlPolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#setrequestheaderpolicy" title="SetRequestHeaderPolicy">SetRequestHeaderPolicy</a>" : <i>[ &lt;a href=&#34;setrequestheaderpolicy.md&#34;&gt;SetRequestHeaderPolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#sslnegotiationpolicy" title="SslNegotiationPolicy">SslNegotiationPolicy</a>" : <i>[ &lt;a href=&#34;sslnegotiationpolicy.md&#34;&gt;SslNegotiationPolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#trustedcertificatepolicy" title="TrustedCertificatePolicy">TrustedCertificatePolicy</a>" : <i>[ &lt;a href=&#34;trustedcertificatepolicy.md&#34;&gt;TrustedCertificatePolicy&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OPC::LbaasPolicy
Properties:
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#loadbalancer" title="LoadBalancer">LoadBalancer</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#applicationcookiestickinesspolicy" title="ApplicationCookieStickinessPolicy">ApplicationCookieStickinessPolicy</a>: <i>
      - &lt;a href=&#34;applicationcookiestickinesspolicy.md&#34;&gt;ApplicationCookieStickinessPolicy&lt;/a&gt;</i>
    <a href="#cloudgatepolicy" title="CloudgatePolicy">CloudgatePolicy</a>: <i>
      - &lt;a href=&#34;cloudgatepolicy.md&#34;&gt;CloudgatePolicy&lt;/a&gt;</i>
    <a href="#loadbalancercookiestickinesspolicy" title="LoadBalancerCookieStickinessPolicy">LoadBalancerCookieStickinessPolicy</a>: <i>
      - &lt;a href=&#34;loadbalancercookiestickinesspolicy.md&#34;&gt;LoadBalancerCookieStickinessPolicy&lt;/a&gt;</i>
    <a href="#loadbalancingmechanismpolicy" title="LoadBalancingMechanismPolicy">LoadBalancingMechanismPolicy</a>: <i>
      - &lt;a href=&#34;loadbalancingmechanismpolicy.md&#34;&gt;LoadBalancingMechanismPolicy&lt;/a&gt;</i>
    <a href="#ratelimitingrequestpolicy" title="RateLimitingRequestPolicy">RateLimitingRequestPolicy</a>: <i>
      - &lt;a href=&#34;ratelimitingrequestpolicy.md&#34;&gt;RateLimitingRequestPolicy&lt;/a&gt;</i>
    <a href="#redirectpolicy" title="RedirectPolicy">RedirectPolicy</a>: <i>
      - &lt;a href=&#34;redirectpolicy.md&#34;&gt;RedirectPolicy&lt;/a&gt;</i>
    <a href="#resourceaccesscontrolpolicy" title="ResourceAccessControlPolicy">ResourceAccessControlPolicy</a>: <i>
      - &lt;a href=&#34;resourceaccesscontrolpolicy.md&#34;&gt;ResourceAccessControlPolicy&lt;/a&gt;</i>
    <a href="#setrequestheaderpolicy" title="SetRequestHeaderPolicy">SetRequestHeaderPolicy</a>: <i>
      - &lt;a href=&#34;setrequestheaderpolicy.md&#34;&gt;SetRequestHeaderPolicy&lt;/a&gt;</i>
    <a href="#sslnegotiationpolicy" title="SslNegotiationPolicy">SslNegotiationPolicy</a>: <i>
      - &lt;a href=&#34;sslnegotiationpolicy.md&#34;&gt;SslNegotiationPolicy&lt;/a&gt;</i>
    <a href="#trustedcertificatepolicy" title="TrustedCertificatePolicy">TrustedCertificatePolicy</a>: <i>
      - &lt;a href=&#34;trustedcertificatepolicy.md&#34;&gt;TrustedCertificatePolicy&lt;/a&gt;</i>
</pre>

## Properties

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancer

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationCookieStickinessPolicy

_Required_: No

_Type_: List of &lt;a href=&#34;applicationcookiestickinesspolicy.md&#34;&gt;ApplicationCookieStickinessPolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudgatePolicy

_Required_: No

_Type_: List of &lt;a href=&#34;cloudgatepolicy.md&#34;&gt;CloudgatePolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerCookieStickinessPolicy

_Required_: No

_Type_: List of &lt;a href=&#34;loadbalancercookiestickinesspolicy.md&#34;&gt;LoadBalancerCookieStickinessPolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancingMechanismPolicy

_Required_: No

_Type_: List of &lt;a href=&#34;loadbalancingmechanismpolicy.md&#34;&gt;LoadBalancingMechanismPolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RateLimitingRequestPolicy

_Required_: No

_Type_: List of &lt;a href=&#34;ratelimitingrequestpolicy.md&#34;&gt;RateLimitingRequestPolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedirectPolicy

_Required_: No

_Type_: List of &lt;a href=&#34;redirectpolicy.md&#34;&gt;RedirectPolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceAccessControlPolicy

_Required_: No

_Type_: List of &lt;a href=&#34;resourceaccesscontrolpolicy.md&#34;&gt;ResourceAccessControlPolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetRequestHeaderPolicy

_Required_: No

_Type_: List of &lt;a href=&#34;setrequestheaderpolicy.md&#34;&gt;SetRequestHeaderPolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslNegotiationPolicy

_Required_: No

_Type_: List of &lt;a href=&#34;sslnegotiationpolicy.md&#34;&gt;SslNegotiationPolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrustedCertificatePolicy

_Required_: No

_Type_: List of &lt;a href=&#34;trustedcertificatepolicy.md&#34;&gt;TrustedCertificatePolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### State

Returns the &lt;code&gt;State&lt;/code&gt; value.

#### Type

Returns the &lt;code&gt;Type&lt;/code&gt; value.

#### Uri

Returns the &lt;code&gt;Uri&lt;/code&gt; value.

