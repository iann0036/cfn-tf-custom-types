# Terraform::AzureRM::ApplicationGateway RewriteRule ResponseHeaderConfiguration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#headername" title="HeaderName">HeaderName</a>" : <i>String</i>,
    "<a href="#headervalue" title="HeaderValue">HeaderValue</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#headername" title="HeaderName">HeaderName</a>: <i>String</i>
<a href="#headervalue" title="HeaderValue">HeaderValue</a>: <i>String</i>
</pre>

## Properties

#### HeaderName

Header name of the header configuration.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeaderValue

Header value of the header configuration. To delete a response header set this property to an empty string.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

