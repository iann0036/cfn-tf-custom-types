# Terraform::OPC::LbaasPolicy

The `opc_lbaas_policy` resource creates and manages a Load Balancer Classic Policy for a Load Balancer Classic instance.

The Policy resource supports the definition of distinct Policy types:

- [Application Cookie Stickiness Policy](#application-cookie-stickiness-policy)
- [CloudGate Policy](#cloudgate-policy)
- [Load Balancer Cookie Stickiness Policy](#load-balancer-cookie-stickiness-policy)
- [Load Balancing Mechanism Policy](#load-balancing-mechanism-policy)
- [Rate Limiting Request Policy](#rate-limiting-request-policy)
- [Redirect Policy](#redirect-policy)
- [Resource Access Control Policy](#resource-access-control-policy)
- [Set Request Header Policy](#set-request-header-policy)
- [SSL Negotiation Policy](#set-negotiation-policy)
- [Trusted Certificate Policy](#trusted-certificate-policy)

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OPC::LbaasPolicy",
    "Properties" : {
        "<a href="#loadbalancer" title="LoadBalancer">LoadBalancer</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#applicationcookiestickinesspolicy" title="ApplicationCookieStickinessPolicy">ApplicationCookieStickinessPolicy</a>" : <i>[ <a href="applicationcookiestickinesspolicy.md">ApplicationCookieStickinessPolicy</a>, ... ]</i>,
        "<a href="#cloudgatepolicy" title="CloudgatePolicy">CloudgatePolicy</a>" : <i>[ <a href="cloudgatepolicy.md">CloudgatePolicy</a>, ... ]</i>,
        "<a href="#loadbalancercookiestickinesspolicy" title="LoadBalancerCookieStickinessPolicy">LoadBalancerCookieStickinessPolicy</a>" : <i>[ <a href="loadbalancercookiestickinesspolicy.md">LoadBalancerCookieStickinessPolicy</a>, ... ]</i>,
        "<a href="#loadbalancingmechanismpolicy" title="LoadBalancingMechanismPolicy">LoadBalancingMechanismPolicy</a>" : <i>[ <a href="loadbalancingmechanismpolicy.md">LoadBalancingMechanismPolicy</a>, ... ]</i>,
        "<a href="#ratelimitingrequestpolicy" title="RateLimitingRequestPolicy">RateLimitingRequestPolicy</a>" : <i>[ <a href="ratelimitingrequestpolicy.md">RateLimitingRequestPolicy</a>, ... ]</i>,
        "<a href="#redirectpolicy" title="RedirectPolicy">RedirectPolicy</a>" : <i>[ <a href="redirectpolicy.md">RedirectPolicy</a>, ... ]</i>,
        "<a href="#resourceaccesscontrolpolicy" title="ResourceAccessControlPolicy">ResourceAccessControlPolicy</a>" : <i>[ <a href="resourceaccesscontrolpolicy.md">ResourceAccessControlPolicy</a>, ... ]</i>,
        "<a href="#setrequestheaderpolicy" title="SetRequestHeaderPolicy">SetRequestHeaderPolicy</a>" : <i>[ <a href="setrequestheaderpolicy.md">SetRequestHeaderPolicy</a>, ... ]</i>,
        "<a href="#sslnegotiationpolicy" title="SslNegotiationPolicy">SslNegotiationPolicy</a>" : <i>[ <a href="sslnegotiationpolicy.md">SslNegotiationPolicy</a>, ... ]</i>,
        "<a href="#trustedcertificatepolicy" title="TrustedCertificatePolicy">TrustedCertificatePolicy</a>" : <i>[ <a href="trustedcertificatepolicy.md">TrustedCertificatePolicy</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OPC::LbaasPolicy
Properties:
    <a href="#loadbalancer" title="LoadBalancer">LoadBalancer</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#applicationcookiestickinesspolicy" title="ApplicationCookieStickinessPolicy">ApplicationCookieStickinessPolicy</a>: <i>
      - <a href="applicationcookiestickinesspolicy.md">ApplicationCookieStickinessPolicy</a></i>
    <a href="#cloudgatepolicy" title="CloudgatePolicy">CloudgatePolicy</a>: <i>
      - <a href="cloudgatepolicy.md">CloudgatePolicy</a></i>
    <a href="#loadbalancercookiestickinesspolicy" title="LoadBalancerCookieStickinessPolicy">LoadBalancerCookieStickinessPolicy</a>: <i>
      - <a href="loadbalancercookiestickinesspolicy.md">LoadBalancerCookieStickinessPolicy</a></i>
    <a href="#loadbalancingmechanismpolicy" title="LoadBalancingMechanismPolicy">LoadBalancingMechanismPolicy</a>: <i>
      - <a href="loadbalancingmechanismpolicy.md">LoadBalancingMechanismPolicy</a></i>
    <a href="#ratelimitingrequestpolicy" title="RateLimitingRequestPolicy">RateLimitingRequestPolicy</a>: <i>
      - <a href="ratelimitingrequestpolicy.md">RateLimitingRequestPolicy</a></i>
    <a href="#redirectpolicy" title="RedirectPolicy">RedirectPolicy</a>: <i>
      - <a href="redirectpolicy.md">RedirectPolicy</a></i>
    <a href="#resourceaccesscontrolpolicy" title="ResourceAccessControlPolicy">ResourceAccessControlPolicy</a>: <i>
      - <a href="resourceaccesscontrolpolicy.md">ResourceAccessControlPolicy</a></i>
    <a href="#setrequestheaderpolicy" title="SetRequestHeaderPolicy">SetRequestHeaderPolicy</a>: <i>
      - <a href="setrequestheaderpolicy.md">SetRequestHeaderPolicy</a></i>
    <a href="#sslnegotiationpolicy" title="SslNegotiationPolicy">SslNegotiationPolicy</a>: <i>
      - <a href="sslnegotiationpolicy.md">SslNegotiationPolicy</a></i>
    <a href="#trustedcertificatepolicy" title="TrustedCertificatePolicy">TrustedCertificatePolicy</a>: <i>
      - <a href="trustedcertificatepolicy.md">TrustedCertificatePolicy</a></i>
</pre>

## Properties

#### LoadBalancer

The parent Load Balancer the Listener.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Listener.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationCookieStickinessPolicy

_Required_: No

_Type_: List of <a href="applicationcookiestickinesspolicy.md">ApplicationCookieStickinessPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudgatePolicy

_Required_: No

_Type_: List of <a href="cloudgatepolicy.md">CloudgatePolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerCookieStickinessPolicy

_Required_: No

_Type_: List of <a href="loadbalancercookiestickinesspolicy.md">LoadBalancerCookieStickinessPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancingMechanismPolicy

_Required_: No

_Type_: List of <a href="loadbalancingmechanismpolicy.md">LoadBalancingMechanismPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RateLimitingRequestPolicy

_Required_: No

_Type_: List of <a href="ratelimitingrequestpolicy.md">RateLimitingRequestPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedirectPolicy

_Required_: No

_Type_: List of <a href="redirectpolicy.md">RedirectPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceAccessControlPolicy

_Required_: No

_Type_: List of <a href="resourceaccesscontrolpolicy.md">ResourceAccessControlPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetRequestHeaderPolicy

_Required_: No

_Type_: List of <a href="setrequestheaderpolicy.md">SetRequestHeaderPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslNegotiationPolicy

_Required_: No

_Type_: List of <a href="sslnegotiationpolicy.md">SslNegotiationPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrustedCertificatePolicy

_Required_: No

_Type_: List of <a href="trustedcertificatepolicy.md">TrustedCertificatePolicy</a>

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

#### State

Returns the <code>State</code> value.

#### Type

Returns the <code>Type</code> value.

#### Uri

Returns the <code>Uri</code> value.

