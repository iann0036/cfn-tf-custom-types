# TF::HCloud::LoadBalancerService HttpDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
    "<a href="#path" title="Path">Path</a>" : <i>String</i>,
    "<a href="#response" title="Response">Response</a>" : <i>String</i>,
    "<a href="#statuscodes" title="StatusCodes">StatusCodes</a>" : <i>[ String, ... ]</i>,
    "<a href="#tls" title="Tls">Tls</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#domain" title="Domain">Domain</a>: <i>String</i>
<a href="#path" title="Path">Path</a>: <i>String</i>
<a href="#response" title="Response">Response</a>: <i>String</i>
<a href="#statuscodes" title="StatusCodes">StatusCodes</a>: <i>
      - String</i>
<a href="#tls" title="Tls">Tls</a>: <i>Boolean</i>
</pre>

## Properties

#### Domain

Domain we try to access when performing the Health Check.
- `path` - (Optional, string) Path we try to access when performing the Health Check.
- `response` - (Optional, string) Response we expect to be included in the Target response when a Health Check was performed.
- `tls` - (Optional, bool) Enable TLS certificate checking.
- `status_codes` - (Optional, list[string]) We expect that the target answers with these status codes. If not the target is marked as `unhealthy`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

Path we try to access when performing the Health Check.
- `response` - (Optional, string) Response we expect to be included in the Target response when a Health Check was performed.
- `tls` - (Optional, bool) Enable TLS certificate checking.
- `status_codes` - (Optional, list[string]) We expect that the target answers with these status codes. If not the target is marked as `unhealthy`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Response

Response we expect to be included in the Target response when a Health Check was performed.
- `tls` - (Optional, bool) Enable TLS certificate checking.
- `status_codes` - (Optional, list[string]) We expect that the target answers with these status codes. If not the target is marked as `unhealthy`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatusCodes

We expect that the target answers with these status codes. If not the target is marked as `unhealthy`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tls

Enable TLS certificate checking.
- `status_codes` - (Optional, list[string]) We expect that the target answers with these status codes. If not the target is marked as `unhealthy`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

