# TF::Datadog::SyntheticsTest

CloudFormation equivalent of datadog_synthetics_test

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Datadog::SyntheticsTest",
    "Properties" : {
        "<a href="#deviceids" title="DeviceIds">DeviceIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#locations" title="Locations">Locations</a>" : <i>[ String, ... ]</i>,
        "<a href="#message" title="Message">Message</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#requestheaders" title="RequestHeaders">RequestHeaders</a>" : <i>[ <a href="requestheadersdefinition.md">RequestHeadersDefinition</a>, ... ]</i>,
        "<a href="#requestquery" title="RequestQuery">RequestQuery</a>" : <i>[ <a href="requestquerydefinition.md">RequestQueryDefinition</a>, ... ]</i>,
        "<a href="#setcookie" title="SetCookie">SetCookie</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#subtype" title="Subtype">Subtype</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#apistep" title="ApiStep">ApiStep</a>" : <i>[ <a href="apistepdefinition.md">ApiStepDefinition</a>, ... ]</i>,
        "<a href="#assertion" title="Assertion">Assertion</a>" : <i>[ <a href="assertiondefinition.md">AssertionDefinition</a>, ... ]</i>,
        "<a href="#browserstep" title="BrowserStep">BrowserStep</a>" : <i>[ <a href="browserstepdefinition.md">BrowserStepDefinition</a>, ... ]</i>,
        "<a href="#browservariable" title="BrowserVariable">BrowserVariable</a>" : <i>[ <a href="browservariabledefinition.md">BrowserVariableDefinition</a>, ... ]</i>,
        "<a href="#configvariable" title="ConfigVariable">ConfigVariable</a>" : <i>[ <a href="configvariabledefinition.md">ConfigVariableDefinition</a>, ... ]</i>,
        "<a href="#optionslist" title="OptionsList">OptionsList</a>" : <i>[ <a href="optionslistdefinition.md">OptionsListDefinition</a>, ... ]</i>,
        "<a href="#requestbasicauth" title="RequestBasicauth">RequestBasicauth</a>" : <i>[ <a href="requestbasicauthdefinition.md">RequestBasicauthDefinition</a>, ... ]</i>,
        "<a href="#requestclientcertificate" title="RequestClientCertificate">RequestClientCertificate</a>" : <i>[ <a href="requestclientcertificatedefinition.md">RequestClientCertificateDefinition</a>, ... ]</i>,
        "<a href="#requestdefinition" title="RequestDefinition">RequestDefinition</a>" : <i>[ <a href="requestdefinitiondefinition.md">RequestDefinitionDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Datadog::SyntheticsTest
Properties:
    <a href="#deviceids" title="DeviceIds">DeviceIds</a>: <i>
      - String</i>
    <a href="#locations" title="Locations">Locations</a>: <i>
      - String</i>
    <a href="#message" title="Message">Message</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#requestheaders" title="RequestHeaders">RequestHeaders</a>: <i>
      - <a href="requestheadersdefinition.md">RequestHeadersDefinition</a></i>
    <a href="#requestquery" title="RequestQuery">RequestQuery</a>: <i>
      - <a href="requestquerydefinition.md">RequestQueryDefinition</a></i>
    <a href="#setcookie" title="SetCookie">SetCookie</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#subtype" title="Subtype">Subtype</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#apistep" title="ApiStep">ApiStep</a>: <i>
      - <a href="apistepdefinition.md">ApiStepDefinition</a></i>
    <a href="#assertion" title="Assertion">Assertion</a>: <i>
      - <a href="assertiondefinition.md">AssertionDefinition</a></i>
    <a href="#browserstep" title="BrowserStep">BrowserStep</a>: <i>
      - <a href="browserstepdefinition.md">BrowserStepDefinition</a></i>
    <a href="#browservariable" title="BrowserVariable">BrowserVariable</a>: <i>
      - <a href="browservariabledefinition.md">BrowserVariableDefinition</a></i>
    <a href="#configvariable" title="ConfigVariable">ConfigVariable</a>: <i>
      - <a href="configvariabledefinition.md">ConfigVariableDefinition</a></i>
    <a href="#optionslist" title="OptionsList">OptionsList</a>: <i>
      - <a href="optionslistdefinition.md">OptionsListDefinition</a></i>
    <a href="#requestbasicauth" title="RequestBasicauth">RequestBasicauth</a>: <i>
      - <a href="requestbasicauthdefinition.md">RequestBasicauthDefinition</a></i>
    <a href="#requestclientcertificate" title="RequestClientCertificate">RequestClientCertificate</a>: <i>
      - <a href="requestclientcertificatedefinition.md">RequestClientCertificateDefinition</a></i>
    <a href="#requestdefinition" title="RequestDefinition">RequestDefinition</a>: <i>
      - <a href="requestdefinitiondefinition.md">RequestDefinitionDefinition</a></i>
</pre>

## Properties

#### DeviceIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Locations

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Message

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestHeaders

_Required_: No

_Type_: List of <a href="requestheadersdefinition.md">RequestHeadersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestQuery

_Required_: No

_Type_: List of <a href="requestquerydefinition.md">RequestQueryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetCookie

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subtype

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApiStep

_Required_: No

_Type_: List of <a href="apistepdefinition.md">ApiStepDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Assertion

_Required_: No

_Type_: List of <a href="assertiondefinition.md">AssertionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BrowserStep

_Required_: No

_Type_: List of <a href="browserstepdefinition.md">BrowserStepDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BrowserVariable

_Required_: No

_Type_: List of <a href="browservariabledefinition.md">BrowserVariableDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigVariable

_Required_: No

_Type_: List of <a href="configvariabledefinition.md">ConfigVariableDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OptionsList

_Required_: No

_Type_: List of <a href="optionslistdefinition.md">OptionsListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestBasicauth

_Required_: No

_Type_: List of <a href="requestbasicauthdefinition.md">RequestBasicauthDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestClientCertificate

_Required_: No

_Type_: List of <a href="requestclientcertificatedefinition.md">RequestClientCertificateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestDefinition

_Required_: No

_Type_: List of <a href="requestdefinitiondefinition.md">RequestDefinitionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### MonitorId

Returns the <code>MonitorId</code> value.

