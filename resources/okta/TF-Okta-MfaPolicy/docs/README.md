# TF::Okta::MfaPolicy

CloudFormation equivalent of okta_mfa_policy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Okta::MfaPolicy",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#duo" title="Duo">Duo</a>" : <i>[ <a href="duodefinition.md">DuoDefinition</a>, ... ]</i>,
        "<a href="#fidou2f" title="FidoU2f">FidoU2f</a>" : <i>[ <a href="fidou2fdefinition.md">FidoU2fDefinition</a>, ... ]</i>,
        "<a href="#fidowebauthn" title="FidoWebauthn">FidoWebauthn</a>" : <i>[ <a href="fidowebauthndefinition.md">FidoWebauthnDefinition</a>, ... ]</i>,
        "<a href="#googleotp" title="GoogleOtp">GoogleOtp</a>" : <i>[ <a href="googleotpdefinition.md">GoogleOtpDefinition</a>, ... ]</i>,
        "<a href="#groupsincluded" title="GroupsIncluded">GroupsIncluded</a>" : <i>[ String, ... ]</i>,
        "<a href="#hotp" title="Hotp">Hotp</a>" : <i>[ <a href="hotpdefinition.md">HotpDefinition</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#oktacall" title="OktaCall">OktaCall</a>" : <i>[ <a href="oktacalldefinition.md">OktaCallDefinition</a>, ... ]</i>,
        "<a href="#oktaemail" title="OktaEmail">OktaEmail</a>" : <i>[ <a href="oktaemaildefinition.md">OktaEmailDefinition</a>, ... ]</i>,
        "<a href="#oktaotp" title="OktaOtp">OktaOtp</a>" : <i>[ <a href="oktaotpdefinition.md">OktaOtpDefinition</a>, ... ]</i>,
        "<a href="#oktapassword" title="OktaPassword">OktaPassword</a>" : <i>[ <a href="oktapassworddefinition.md">OktaPasswordDefinition</a>, ... ]</i>,
        "<a href="#oktapush" title="OktaPush">OktaPush</a>" : <i>[ <a href="oktapushdefinition.md">OktaPushDefinition</a>, ... ]</i>,
        "<a href="#oktaquestion" title="OktaQuestion">OktaQuestion</a>" : <i>[ <a href="oktaquestiondefinition.md">OktaQuestionDefinition</a>, ... ]</i>,
        "<a href="#oktasms" title="OktaSms">OktaSms</a>" : <i>[ <a href="oktasmsdefinition.md">OktaSmsDefinition</a>, ... ]</i>,
        "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
        "<a href="#rsatoken" title="RsaToken">RsaToken</a>" : <i>[ <a href="rsatokendefinition.md">RsaTokenDefinition</a>, ... ]</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#symantecvip" title="SymantecVip">SymantecVip</a>" : <i>[ <a href="symantecvipdefinition.md">SymantecVipDefinition</a>, ... ]</i>,
        "<a href="#yubikeytoken" title="YubikeyToken">YubikeyToken</a>" : <i>[ <a href="yubikeytokendefinition.md">YubikeyTokenDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Okta::MfaPolicy
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#duo" title="Duo">Duo</a>: <i>
      - <a href="duodefinition.md">DuoDefinition</a></i>
    <a href="#fidou2f" title="FidoU2f">FidoU2f</a>: <i>
      - <a href="fidou2fdefinition.md">FidoU2fDefinition</a></i>
    <a href="#fidowebauthn" title="FidoWebauthn">FidoWebauthn</a>: <i>
      - <a href="fidowebauthndefinition.md">FidoWebauthnDefinition</a></i>
    <a href="#googleotp" title="GoogleOtp">GoogleOtp</a>: <i>
      - <a href="googleotpdefinition.md">GoogleOtpDefinition</a></i>
    <a href="#groupsincluded" title="GroupsIncluded">GroupsIncluded</a>: <i>
      - String</i>
    <a href="#hotp" title="Hotp">Hotp</a>: <i>
      - <a href="hotpdefinition.md">HotpDefinition</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#oktacall" title="OktaCall">OktaCall</a>: <i>
      - <a href="oktacalldefinition.md">OktaCallDefinition</a></i>
    <a href="#oktaemail" title="OktaEmail">OktaEmail</a>: <i>
      - <a href="oktaemaildefinition.md">OktaEmailDefinition</a></i>
    <a href="#oktaotp" title="OktaOtp">OktaOtp</a>: <i>
      - <a href="oktaotpdefinition.md">OktaOtpDefinition</a></i>
    <a href="#oktapassword" title="OktaPassword">OktaPassword</a>: <i>
      - <a href="oktapassworddefinition.md">OktaPasswordDefinition</a></i>
    <a href="#oktapush" title="OktaPush">OktaPush</a>: <i>
      - <a href="oktapushdefinition.md">OktaPushDefinition</a></i>
    <a href="#oktaquestion" title="OktaQuestion">OktaQuestion</a>: <i>
      - <a href="oktaquestiondefinition.md">OktaQuestionDefinition</a></i>
    <a href="#oktasms" title="OktaSms">OktaSms</a>: <i>
      - <a href="oktasmsdefinition.md">OktaSmsDefinition</a></i>
    <a href="#priority" title="Priority">Priority</a>: <i>Double</i>
    <a href="#rsatoken" title="RsaToken">RsaToken</a>: <i>
      - <a href="rsatokendefinition.md">RsaTokenDefinition</a></i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#symantecvip" title="SymantecVip">SymantecVip</a>: <i>
      - <a href="symantecvipdefinition.md">SymantecVipDefinition</a></i>
    <a href="#yubikeytoken" title="YubikeyToken">YubikeyToken</a>: <i>
      - <a href="yubikeytokendefinition.md">YubikeyTokenDefinition</a></i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Duo

_Required_: No

_Type_: List of <a href="duodefinition.md">DuoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FidoU2f

_Required_: No

_Type_: List of <a href="fidou2fdefinition.md">FidoU2fDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FidoWebauthn

_Required_: No

_Type_: List of <a href="fidowebauthndefinition.md">FidoWebauthnDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GoogleOtp

_Required_: No

_Type_: List of <a href="googleotpdefinition.md">GoogleOtpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupsIncluded

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hotp

_Required_: No

_Type_: List of <a href="hotpdefinition.md">HotpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OktaCall

_Required_: No

_Type_: List of <a href="oktacalldefinition.md">OktaCallDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OktaEmail

_Required_: No

_Type_: List of <a href="oktaemaildefinition.md">OktaEmailDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OktaOtp

_Required_: No

_Type_: List of <a href="oktaotpdefinition.md">OktaOtpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OktaPassword

_Required_: No

_Type_: List of <a href="oktapassworddefinition.md">OktaPasswordDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OktaPush

_Required_: No

_Type_: List of <a href="oktapushdefinition.md">OktaPushDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OktaQuestion

_Required_: No

_Type_: List of <a href="oktaquestiondefinition.md">OktaQuestionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OktaSms

_Required_: No

_Type_: List of <a href="oktasmsdefinition.md">OktaSmsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RsaToken

_Required_: No

_Type_: List of <a href="rsatokendefinition.md">RsaTokenDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SymantecVip

_Required_: No

_Type_: List of <a href="symantecvipdefinition.md">SymantecVipDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### YubikeyToken

_Required_: No

_Type_: List of <a href="yubikeytokendefinition.md">YubikeyTokenDefinition</a>

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

