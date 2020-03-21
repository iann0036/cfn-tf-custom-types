# Terraform::HuaweiCloud::ObsBucket Website

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#errordocument" title="ErrorDocument">ErrorDocument</a>" : <i>String</i>,
    "<a href="#indexdocument" title="IndexDocument">IndexDocument</a>" : <i>String</i>,
    "<a href="#redirectallrequeststo" title="RedirectAllRequestsTo">RedirectAllRequestsTo</a>" : <i>String</i>,
    "<a href="#routingrules" title="RoutingRules">RoutingRules</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#errordocument" title="ErrorDocument">ErrorDocument</a>: <i>String</i>
<a href="#indexdocument" title="IndexDocument">IndexDocument</a>: <i>String</i>
<a href="#redirectallrequeststo" title="RedirectAllRequestsTo">RedirectAllRequestsTo</a>: <i>String</i>
<a href="#routingrules" title="RoutingRules">RoutingRules</a>: <i>String</i>
</pre>

## Properties

#### ErrorDocument

Specifies the error page returned when an error occurs during static website access.
Only HTML, JPG, PNG, BMP, and WEBP files under the root directory are supported.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IndexDocument

Specifies the default homepage of the static website, only HTML web pages are supported.
OBS only allows files such as `index.html` in the root directory of a bucket to function as the default homepage.
That is to say, do not set the default homepage with a multi-level directory structure (for example, /page/index.html).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedirectAllRequestsTo

A hostname to redirect all website requests for this bucket to. Hostname can optionally be prefixed with a protocol (`http://` or `https://`) to use when redirecting requests. The default is the protocol that is used in the original request.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoutingRules

A JSON or XML format containing routing rules describing redirect behavior and when redirects are applied.
Each rule contains a `Condition` and a `Redirect` as shown in the following table:.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

