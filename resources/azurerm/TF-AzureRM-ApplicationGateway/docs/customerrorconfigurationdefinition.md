# TF::AzureRM::ApplicationGateway CustomErrorConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#customerrorpageurl" title="CustomErrorPageUrl">CustomErrorPageUrl</a>" : <i>String</i>,
    "<a href="#statuscode" title="StatusCode">StatusCode</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#customerrorpageurl" title="CustomErrorPageUrl">CustomErrorPageUrl</a>: <i>String</i>
<a href="#statuscode" title="StatusCode">StatusCode</a>: <i>String</i>
</pre>

## Properties

#### CustomErrorPageUrl

Error page URL of the application gateway customer error.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatusCode

Status code of the application gateway customer error. Possible values are `HttpStatus403` and `HttpStatus502`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

