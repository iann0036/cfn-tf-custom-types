# Terraform::AzureStack::StorageAccount CustomDomain

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#usesubdomain" title="UseSubdomain">UseSubdomain</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#usesubdomain" title="UseSubdomain">UseSubdomain</a>: <i>Boolean</i>
</pre>

## Properties

#### Name

The Custom Domain Name to use for the Storage Account, which will be validated by Azure.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseSubdomain

Should the Custom Domain Name be validated by using indirect CNAME validation?.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

