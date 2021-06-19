# TF::FortiOS::Wirelesscontrollerhotspot20Anqpnairealm EapMethodDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#index" title="Index">Index</a>" : <i>Double</i>,
    "<a href="#method" title="Method">Method</a>" : <i>String</i>,
    "<a href="#authparam" title="AuthParam">AuthParam</a>" : <i>[ <a href="authparamdefinition.md">AuthParamDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#index" title="Index">Index</a>: <i>Double</i>
<a href="#method" title="Method">Method</a>: <i>String</i>
<a href="#authparam" title="AuthParam">AuthParam</a>: <i>
      - <a href="authparamdefinition.md">AuthParamDefinition</a></i>
</pre>

## Properties

#### Index

EAP method index.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Method

EAP method type. Valid values: `eap-identity`, `eap-md5`, `eap-tls`, `eap-ttls`, `eap-peap`, `eap-sim`, `eap-aka`, `eap-aka-prime`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthParam

_Required_: No

_Type_: List of <a href="authparamdefinition.md">AuthParamDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

