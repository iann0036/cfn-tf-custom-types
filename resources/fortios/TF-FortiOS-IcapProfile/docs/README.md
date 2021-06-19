# TF::FortiOS::IcapProfile

Configure ICAP profiles.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::IcapProfile",
    "Properties" : {
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#methods" title="Methods">Methods</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#preview" title="Preview">Preview</a>" : <i>String</i>,
        "<a href="#previewdatalength" title="PreviewDataLength">PreviewDataLength</a>" : <i>Double</i>,
        "<a href="#replacemsggroup" title="ReplacemsgGroup">ReplacemsgGroup</a>" : <i>String</i>,
        "<a href="#request" title="Request">Request</a>" : <i>String</i>,
        "<a href="#requestfailure" title="RequestFailure">RequestFailure</a>" : <i>String</i>,
        "<a href="#requestpath" title="RequestPath">RequestPath</a>" : <i>String</i>,
        "<a href="#requestserver" title="RequestServer">RequestServer</a>" : <i>String</i>,
        "<a href="#respmoddefaultaction" title="RespmodDefaultAction">RespmodDefaultAction</a>" : <i>String</i>,
        "<a href="#response" title="Response">Response</a>" : <i>String</i>,
        "<a href="#responsefailure" title="ResponseFailure">ResponseFailure</a>" : <i>String</i>,
        "<a href="#responsepath" title="ResponsePath">ResponsePath</a>" : <i>String</i>,
        "<a href="#responsereqhdr" title="ResponseReqHdr">ResponseReqHdr</a>" : <i>String</i>,
        "<a href="#responseserver" title="ResponseServer">ResponseServer</a>" : <i>String</i>,
        "<a href="#streamingcontentbypass" title="StreamingContentBypass">StreamingContentBypass</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#icapheaders" title="IcapHeaders">IcapHeaders</a>" : <i>[ <a href="icapheadersdefinition.md">IcapHeadersDefinition</a>, ... ]</i>,
        "<a href="#respmodforwardrules" title="RespmodForwardRules">RespmodForwardRules</a>" : <i>[ <a href="respmodforwardrulesdefinition.md">RespmodForwardRulesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::IcapProfile
Properties:
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#methods" title="Methods">Methods</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#preview" title="Preview">Preview</a>: <i>String</i>
    <a href="#previewdatalength" title="PreviewDataLength">PreviewDataLength</a>: <i>Double</i>
    <a href="#replacemsggroup" title="ReplacemsgGroup">ReplacemsgGroup</a>: <i>String</i>
    <a href="#request" title="Request">Request</a>: <i>String</i>
    <a href="#requestfailure" title="RequestFailure">RequestFailure</a>: <i>String</i>
    <a href="#requestpath" title="RequestPath">RequestPath</a>: <i>String</i>
    <a href="#requestserver" title="RequestServer">RequestServer</a>: <i>String</i>
    <a href="#respmoddefaultaction" title="RespmodDefaultAction">RespmodDefaultAction</a>: <i>String</i>
    <a href="#response" title="Response">Response</a>: <i>String</i>
    <a href="#responsefailure" title="ResponseFailure">ResponseFailure</a>: <i>String</i>
    <a href="#responsepath" title="ResponsePath">ResponsePath</a>: <i>String</i>
    <a href="#responsereqhdr" title="ResponseReqHdr">ResponseReqHdr</a>: <i>String</i>
    <a href="#responseserver" title="ResponseServer">ResponseServer</a>: <i>String</i>
    <a href="#streamingcontentbypass" title="StreamingContentBypass">StreamingContentBypass</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#icapheaders" title="IcapHeaders">IcapHeaders</a>: <i>
      - <a href="icapheadersdefinition.md">IcapHeadersDefinition</a></i>
    <a href="#respmodforwardrules" title="RespmodForwardRules">RespmodForwardRules</a>: <i>
      - <a href="respmodforwardrulesdefinition.md">RespmodForwardRulesDefinition</a></i>
</pre>

## Properties

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Methods

The allowed HTTP methods that will be sent to ICAP server for further processing. Valid values: `delete`, `get`, `head`, `options`, `post`, `put`, `trace`, `other`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

ICAP profile name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Preview

Enable/disable preview of data to ICAP server. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreviewDataLength

Preview data length to be sent to ICAP server.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplacemsgGroup

Replacement message group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Request

Enable/disable whether an HTTP request is passed to an ICAP server. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestFailure

Action to take if the ICAP server cannot be contacted when processing an HTTP request. Valid values: `error`, `bypass`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestPath

Path component of the ICAP URI that identifies the HTTP request processing service.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestServer

ICAP server to use for an HTTP request.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RespmodDefaultAction

Default action to ICAP response modification (respmod) processing. Valid values: `forward`, `bypass`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Response

Enable/disable whether an HTTP response is passed to an ICAP server. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseFailure

Action to take if the ICAP server cannot be contacted when processing an HTTP response. Valid values: `error`, `bypass`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponsePath

Path component of the ICAP URI that identifies the HTTP response processing service.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseReqHdr

Enable/disable addition of req-hdr for ICAP response modification (respmod) processing. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseServer

ICAP server to use for an HTTP response.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StreamingContentBypass

Enable/disable bypassing of ICAP server for streaming content. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IcapHeaders

_Required_: No

_Type_: List of <a href="icapheadersdefinition.md">IcapHeadersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RespmodForwardRules

_Required_: No

_Type_: List of <a href="respmodforwardrulesdefinition.md">RespmodForwardRulesDefinition</a>

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

