# Terraform::AzureRM::ApiManagementApi Import

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#contentformat" title="ContentFormat">ContentFormat</a>" : <i>String</i>,
    "<a href="#contentvalue" title="ContentValue">ContentValue</a>" : <i>String</i>,
    "<a href="#wsdlselector" title="WsdlSelector">WsdlSelector</a>" : <i>[ <a href="import-wsdlselector.md">WsdlSelector</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#contentformat" title="ContentFormat">ContentFormat</a>: <i>String</i>
<a href="#contentvalue" title="ContentValue">ContentValue</a>: <i>String</i>
<a href="#wsdlselector" title="WsdlSelector">WsdlSelector</a>: <i>
      - <a href="import-wsdlselector.md">WsdlSelector</a></i>
</pre>

## Properties

#### ContentFormat

The format of the content from which the API Definition should be imported. Possible values are: `swagger-json`, `swagger-link-json`, `wadl-link-json`, `wadl-xml`, `wsdl` and `wsdl-link`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentValue

The Content from which the API Definition should be imported. When a `content_format` of `*-link-*` is specified this must be a URL, otherwise this must be defined inline.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WsdlSelector

_Required_: No

_Type_: List of <a href="import-wsdlselector.md">WsdlSelector</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

