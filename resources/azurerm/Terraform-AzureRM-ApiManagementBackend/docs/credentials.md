# Terraform::AzureRM::ApiManagementBackend Credentials

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#certificate" title="Certificate">Certificate</a>" : <i>[ String, ... ]</i>,
    "<a href="#header" title="Header">Header</a>" : <i>[ <a href="credentials-header.md">Header</a>, ... ]</i>,
    "<a href="#query" title="Query">Query</a>" : <i>[ <a href="credentials-query.md">Query</a>, ... ]</i>,
    "<a href="#authorization" title="Authorization">Authorization</a>" : <i>[ <a href="credentials-authorization.md">Authorization</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#certificate" title="Certificate">Certificate</a>: <i>
      - String</i>
<a href="#header" title="Header">Header</a>: <i>
      - <a href="credentials-header.md">Header</a></i>
<a href="#query" title="Query">Query</a>: <i>
      - <a href="credentials-query.md">Query</a></i>
<a href="#authorization" title="Authorization">Authorization</a>: <i>
      - <a href="credentials-authorization.md">Authorization</a></i>
</pre>

## Properties

#### Certificate

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Header

_Required_: No
_Type_: List of <a href="credentials-header.md">Header</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Query

_Required_: No
_Type_: List of <a href="credentials-query.md">Query</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Authorization

_Required_: No
_Type_: List of <a href="credentials-authorization.md">Authorization</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

