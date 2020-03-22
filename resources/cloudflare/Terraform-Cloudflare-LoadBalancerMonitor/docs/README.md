# Terraform::Cloudflare::LoadBalancerMonitor

If you're using Cloudflare's Load Balancing to load-balance across multiple origin servers or data centers, you configure one of these Monitors to actively check the availability of those servers over HTTP(S) or TCP.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Cloudflare::LoadBalancerMonitor",
    "Properties" : {
        "<a href="#allowinsecure" title="AllowInsecure">AllowInsecure</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#expectedbody" title="ExpectedBody">ExpectedBody</a>" : <i>String</i>,
        "<a href="#expectedcodes" title="ExpectedCodes">ExpectedCodes</a>" : <i>String</i>,
        "<a href="#followredirects" title="FollowRedirects">FollowRedirects</a>" : <i>Boolean</i>,
        "<a href="#interval" title="Interval">Interval</a>" : <i>Double</i>,
        "<a href="#method" title="Method">Method</a>" : <i>String</i>,
        "<a href="#path" title="Path">Path</a>" : <i>String</i>,
        "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
        "<a href="#retries" title="Retries">Retries</a>" : <i>Double</i>,
        "<a href="#timeout" title="Timeout">Timeout</a>" : <i>Double</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#header" title="Header">Header</a>" : <i>[ <a href="header.md">Header</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Cloudflare::LoadBalancerMonitor
Properties:
    <a href="#allowinsecure" title="AllowInsecure">AllowInsecure</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#expectedbody" title="ExpectedBody">ExpectedBody</a>: <i>String</i>
    <a href="#expectedcodes" title="ExpectedCodes">ExpectedCodes</a>: <i>String</i>
    <a href="#followredirects" title="FollowRedirects">FollowRedirects</a>: <i>Boolean</i>
    <a href="#interval" title="Interval">Interval</a>: <i>Double</i>
    <a href="#method" title="Method">Method</a>: <i>String</i>
    <a href="#path" title="Path">Path</a>: <i>String</i>
    <a href="#port" title="Port">Port</a>: <i>Double</i>
    <a href="#retries" title="Retries">Retries</a>: <i>Double</i>
    <a href="#timeout" title="Timeout">Timeout</a>: <i>Double</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#header" title="Header">Header</a>: <i>
      - <a href="header.md">Header</a></i>
</pre>

## Properties

#### AllowInsecure

Do not validate the certificate when monitor use HTTPS. Only valid if `type` is "http" or "https".

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Free text description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpectedBody

A case-insensitive sub-string to look for in the response body. If this string is not found, the origin will be marked as unhealthy. Only valid if `type` is "http" or "https". Default: "".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpectedCodes

The expected HTTP response code or code range of the health check. Eg `2xx`. Only valid and required if `type` is "http" or "https".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FollowRedirects

Follow redirects if returned by the origin. Only valid if `type` is "http" or "https".

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interval

The interval between each health check. Shorter intervals may improve failover time, but will increase load on the origins as we check from multiple locations. Default: 60.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Method

The method to use for the health check. Valid values are any valid HTTP verb if `type` is "http" or "https", or `connection_established` if `type` is "tcp". Default: "GET" if `type` is "http" or "https", or "connection_established" if `type` is "tcp" .

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

The endpoint path to health check against. Default: "/". Only valid if `type` is "http" or "https".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Retries

The number of retries to attempt in case of a timeout before marking the origin as unhealthy. Retries are attempted immediately. Default: 2.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

The timeout (in seconds) before marking the health check as failed. Default: 5.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The protocol to use for the healthcheck. Currently supported protocols are 'HTTP', 'HTTPS' and 'TCP'. Default: "http".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Header

_Required_: No

_Type_: List of <a href="header.md">Header</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreatedOn

Returns the <code>CreatedOn</code> value.

#### Id

Returns the <code>Id</code> value.

#### ModifiedOn

Returns the <code>ModifiedOn</code> value.

