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

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentValue

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WsdlSelector

_Required_: No

_Type_: List of <a href="import-wsdlselector.md">WsdlSelector</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

