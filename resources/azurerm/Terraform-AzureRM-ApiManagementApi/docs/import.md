# Terraform::AzureRM::ApiManagementApi Import

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#contentformat" title="ContentFormat">ContentFormat</a>" : <i>String</i>,
    "<a href="#contentvalue" title="ContentValue">ContentValue</a>" : <i>String</i>,
    "<a href="#wsdlselector" title="WsdlSelector">WsdlSelector</a>" : <i>[ &lt;a href=&#34;import-wsdlselector.md&#34;&gt;WsdlSelector&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#contentformat" title="ContentFormat">ContentFormat</a>: <i>String</i>
<a href="#contentvalue" title="ContentValue">ContentValue</a>: <i>String</i>
<a href="#wsdlselector" title="WsdlSelector">WsdlSelector</a>: <i>
      - &lt;a href=&#34;import-wsdlselector.md&#34;&gt;WsdlSelector&lt;/a&gt;</i>
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
_Type_: List of &lt;a href=&#34;import-wsdlselector.md&#34;&gt;WsdlSelector&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

