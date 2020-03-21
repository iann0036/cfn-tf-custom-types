# Terraform::HuaweiCloud::S3Bucket Website

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

An absolute path to the document to return in case of a 4XX error.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IndexDocument

Amazon S3 returns this index document when requests are made to the root domain or any of the subfolders.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedirectAllRequestsTo

A hostname to redirect all website requests for this bucket to. Hostname can optionally be prefixed with a protocol (`http://` or `https://`) to use when redirecting requests. The default is the protocol that is used in the original request.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoutingRules

A json array containing [routing rules](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-websiteconfiguration-routingrules.html)
describing redirect behavior and when redirects are applied.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

