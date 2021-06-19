# TF::Thunder::FwRadiusServer

`thunder_fw_radius_server` Provides details about thunder fw radius server

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::FwRadiusServer",
    "Properties" : {
        "<a href="#accountinginterimupdate" title="AccountingInterimUpdate">AccountingInterimUpdate</a>" : <i>String</i>,
        "<a href="#accountingon" title="AccountingOn">AccountingOn</a>" : <i>String</i>,
        "<a href="#accountingstart" title="AccountingStart">AccountingStart</a>" : <i>String</i>,
        "<a href="#accountingstop" title="AccountingStop">AccountingStop</a>" : <i>String</i>,
        "<a href="#attributename" title="AttributeName">AttributeName</a>" : <i>String</i>,
        "<a href="#customattributename" title="CustomAttributeName">CustomAttributeName</a>" : <i>String</i>,
        "<a href="#encrypted" title="Encrypted">Encrypted</a>" : <i>String</i>,
        "<a href="#listenport" title="ListenPort">ListenPort</a>" : <i>Double</i>,
        "<a href="#secret" title="Secret">Secret</a>" : <i>Double</i>,
        "<a href="#secretstring" title="SecretString">SecretString</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#vrid" title="Vrid">Vrid</a>" : <i>Double</i>,
        "<a href="#attribute" title="Attribute">Attribute</a>" : <i>[ <a href="attributedefinition.md">AttributeDefinition</a>, ... ]</i>,
        "<a href="#remote" title="Remote">Remote</a>" : <i>[ <a href="remotedefinition.md">RemoteDefinition</a>, ... ]</i>,
        "<a href="#samplingenable" title="SamplingEnable">SamplingEnable</a>" : <i>[ <a href="samplingenabledefinition.md">SamplingEnableDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::FwRadiusServer
Properties:
    <a href="#accountinginterimupdate" title="AccountingInterimUpdate">AccountingInterimUpdate</a>: <i>String</i>
    <a href="#accountingon" title="AccountingOn">AccountingOn</a>: <i>String</i>
    <a href="#accountingstart" title="AccountingStart">AccountingStart</a>: <i>String</i>
    <a href="#accountingstop" title="AccountingStop">AccountingStop</a>: <i>String</i>
    <a href="#attributename" title="AttributeName">AttributeName</a>: <i>String</i>
    <a href="#customattributename" title="CustomAttributeName">CustomAttributeName</a>: <i>String</i>
    <a href="#encrypted" title="Encrypted">Encrypted</a>: <i>String</i>
    <a href="#listenport" title="ListenPort">ListenPort</a>: <i>Double</i>
    <a href="#secret" title="Secret">Secret</a>: <i>Double</i>
    <a href="#secretstring" title="SecretString">SecretString</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#vrid" title="Vrid">Vrid</a>: <i>Double</i>
    <a href="#attribute" title="Attribute">Attribute</a>: <i>
      - <a href="attributedefinition.md">AttributeDefinition</a></i>
    <a href="#remote" title="Remote">Remote</a>: <i>
      - <a href="remotedefinition.md">RemoteDefinition</a></i>
    <a href="#samplingenable" title="SamplingEnable">SamplingEnable</a>: <i>
      - <a href="samplingenabledefinition.md">SamplingEnableDefinition</a></i>
</pre>

## Properties

#### AccountingInterimUpdate

‘ignore’: Ignore (default); ‘append-entry’: Append the AVPs to existing entry; ‘replace-entry’: Replace the AVPs of existing entry;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountingOn

‘ignore’: Ignore (default); ‘delete-entries-using-attribute’: Delete entries matching attribute in RADIUS Table;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountingStart

‘ignore’: Ignore; ‘append-entry’: Append the AVPs to existing entry (default); ‘replace-entry’: Replace the AVPs of existing entry;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountingStop

‘ignore’: Ignore; ‘delete-entry’: Delete the entry (default);.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AttributeName

‘msisdn’: Clear using MSISDN; ‘imei’: Clear using IMEI; ‘imsi’: Clear using IMSI;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomAttributeName

Clear using customized attribute.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Encrypted

Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED secret string).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ListenPort

Configure the listen port of RADIUS server (Port number).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Secret

Configure shared secret.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretString

The RADIUS secret.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vrid

Join a VRRP-A failover group.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Attribute

_Required_: No

_Type_: List of <a href="attributedefinition.md">AttributeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Remote

_Required_: No

_Type_: List of <a href="remotedefinition.md">RemoteDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SamplingEnable

_Required_: No

_Type_: List of <a href="samplingenabledefinition.md">SamplingEnableDefinition</a>

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

