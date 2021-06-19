# TF::FortiOS::VoipProfile SipDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ackrate" title="AckRate">AckRate</a>" : <i>Double</i>,
    "<a href="#blockack" title="BlockAck">BlockAck</a>" : <i>String</i>,
    "<a href="#blockbye" title="BlockBye">BlockBye</a>" : <i>String</i>,
    "<a href="#blockcancel" title="BlockCancel">BlockCancel</a>" : <i>String</i>,
    "<a href="#blockgeoredoptions" title="BlockGeoRedOptions">BlockGeoRedOptions</a>" : <i>String</i>,
    "<a href="#blockinfo" title="BlockInfo">BlockInfo</a>" : <i>String</i>,
    "<a href="#blockinvite" title="BlockInvite">BlockInvite</a>" : <i>String</i>,
    "<a href="#blocklonglines" title="BlockLongLines">BlockLongLines</a>" : <i>String</i>,
    "<a href="#blockmessage" title="BlockMessage">BlockMessage</a>" : <i>String</i>,
    "<a href="#blocknotify" title="BlockNotify">BlockNotify</a>" : <i>String</i>,
    "<a href="#blockoptions" title="BlockOptions">BlockOptions</a>" : <i>String</i>,
    "<a href="#blockprack" title="BlockPrack">BlockPrack</a>" : <i>String</i>,
    "<a href="#blockpublish" title="BlockPublish">BlockPublish</a>" : <i>String</i>,
    "<a href="#blockrefer" title="BlockRefer">BlockRefer</a>" : <i>String</i>,
    "<a href="#blockregister" title="BlockRegister">BlockRegister</a>" : <i>String</i>,
    "<a href="#blocksubscribe" title="BlockSubscribe">BlockSubscribe</a>" : <i>String</i>,
    "<a href="#blockunknown" title="BlockUnknown">BlockUnknown</a>" : <i>String</i>,
    "<a href="#blockupdate" title="BlockUpdate">BlockUpdate</a>" : <i>String</i>,
    "<a href="#byerate" title="ByeRate">ByeRate</a>" : <i>Double</i>,
    "<a href="#callkeepalive" title="CallKeepalive">CallKeepalive</a>" : <i>Double</i>,
    "<a href="#cancelrate" title="CancelRate">CancelRate</a>" : <i>Double</i>,
    "<a href="#contactfixup" title="ContactFixup">ContactFixup</a>" : <i>String</i>,
    "<a href="#hntrestrictsourceip" title="HntRestrictSourceIp">HntRestrictSourceIp</a>" : <i>String</i>,
    "<a href="#hostednattraversal" title="HostedNatTraversal">HostedNatTraversal</a>" : <i>String</i>,
    "<a href="#inforate" title="InfoRate">InfoRate</a>" : <i>Double</i>,
    "<a href="#inviterate" title="InviteRate">InviteRate</a>" : <i>Double</i>,
    "<a href="#ipsrtp" title="IpsRtp">IpsRtp</a>" : <i>String</i>,
    "<a href="#logcallsummary" title="LogCallSummary">LogCallSummary</a>" : <i>String</i>,
    "<a href="#logviolations" title="LogViolations">LogViolations</a>" : <i>String</i>,
    "<a href="#malformedheaderallow" title="MalformedHeaderAllow">MalformedHeaderAllow</a>" : <i>String</i>,
    "<a href="#malformedheadercallid" title="MalformedHeaderCallId">MalformedHeaderCallId</a>" : <i>String</i>,
    "<a href="#malformedheadercontact" title="MalformedHeaderContact">MalformedHeaderContact</a>" : <i>String</i>,
    "<a href="#malformedheadercontentlength" title="MalformedHeaderContentLength">MalformedHeaderContentLength</a>" : <i>String</i>,
    "<a href="#malformedheadercontenttype" title="MalformedHeaderContentType">MalformedHeaderContentType</a>" : <i>String</i>,
    "<a href="#malformedheadercseq" title="MalformedHeaderCseq">MalformedHeaderCseq</a>" : <i>String</i>,
    "<a href="#malformedheaderexpires" title="MalformedHeaderExpires">MalformedHeaderExpires</a>" : <i>String</i>,
    "<a href="#malformedheaderfrom" title="MalformedHeaderFrom">MalformedHeaderFrom</a>" : <i>String</i>,
    "<a href="#malformedheadermaxforwards" title="MalformedHeaderMaxForwards">MalformedHeaderMaxForwards</a>" : <i>String</i>,
    "<a href="#malformedheaderpassertedidentity" title="MalformedHeaderPAssertedIdentity">MalformedHeaderPAssertedIdentity</a>" : <i>String</i>,
    "<a href="#malformedheaderrack" title="MalformedHeaderRack">MalformedHeaderRack</a>" : <i>String</i>,
    "<a href="#malformedheaderrecordroute" title="MalformedHeaderRecordRoute">MalformedHeaderRecordRoute</a>" : <i>String</i>,
    "<a href="#malformedheaderroute" title="MalformedHeaderRoute">MalformedHeaderRoute</a>" : <i>String</i>,
    "<a href="#malformedheaderrseq" title="MalformedHeaderRseq">MalformedHeaderRseq</a>" : <i>String</i>,
    "<a href="#malformedheadersdpa" title="MalformedHeaderSdpA">MalformedHeaderSdpA</a>" : <i>String</i>,
    "<a href="#malformedheadersdpb" title="MalformedHeaderSdpB">MalformedHeaderSdpB</a>" : <i>String</i>,
    "<a href="#malformedheadersdpc" title="MalformedHeaderSdpC">MalformedHeaderSdpC</a>" : <i>String</i>,
    "<a href="#malformedheadersdpi" title="MalformedHeaderSdpI">MalformedHeaderSdpI</a>" : <i>String</i>,
    "<a href="#malformedheadersdpk" title="MalformedHeaderSdpK">MalformedHeaderSdpK</a>" : <i>String</i>,
    "<a href="#malformedheadersdpm" title="MalformedHeaderSdpM">MalformedHeaderSdpM</a>" : <i>String</i>,
    "<a href="#malformedheadersdpo" title="MalformedHeaderSdpO">MalformedHeaderSdpO</a>" : <i>String</i>,
    "<a href="#malformedheadersdpr" title="MalformedHeaderSdpR">MalformedHeaderSdpR</a>" : <i>String</i>,
    "<a href="#malformedheadersdps" title="MalformedHeaderSdpS">MalformedHeaderSdpS</a>" : <i>String</i>,
    "<a href="#malformedheadersdpt" title="MalformedHeaderSdpT">MalformedHeaderSdpT</a>" : <i>String</i>,
    "<a href="#malformedheadersdpv" title="MalformedHeaderSdpV">MalformedHeaderSdpV</a>" : <i>String</i>,
    "<a href="#malformedheadersdpz" title="MalformedHeaderSdpZ">MalformedHeaderSdpZ</a>" : <i>String</i>,
    "<a href="#malformedheaderto" title="MalformedHeaderTo">MalformedHeaderTo</a>" : <i>String</i>,
    "<a href="#malformedheadervia" title="MalformedHeaderVia">MalformedHeaderVia</a>" : <i>String</i>,
    "<a href="#malformedrequestline" title="MalformedRequestLine">MalformedRequestLine</a>" : <i>String</i>,
    "<a href="#maxbodylength" title="MaxBodyLength">MaxBodyLength</a>" : <i>Double</i>,
    "<a href="#maxdialogs" title="MaxDialogs">MaxDialogs</a>" : <i>Double</i>,
    "<a href="#maxidledialogs" title="MaxIdleDialogs">MaxIdleDialogs</a>" : <i>Double</i>,
    "<a href="#maxlinelength" title="MaxLineLength">MaxLineLength</a>" : <i>Double</i>,
    "<a href="#messagerate" title="MessageRate">MessageRate</a>" : <i>Double</i>,
    "<a href="#natportrange" title="NatPortRange">NatPortRange</a>" : <i>String</i>,
    "<a href="#nattrace" title="NatTrace">NatTrace</a>" : <i>String</i>,
    "<a href="#nosdpfixup" title="NoSdpFixup">NoSdpFixup</a>" : <i>String</i>,
    "<a href="#notifyrate" title="NotifyRate">NotifyRate</a>" : <i>Double</i>,
    "<a href="#opencontactpinhole" title="OpenContactPinhole">OpenContactPinhole</a>" : <i>String</i>,
    "<a href="#openrecordroutepinhole" title="OpenRecordRoutePinhole">OpenRecordRoutePinhole</a>" : <i>String</i>,
    "<a href="#openregisterpinhole" title="OpenRegisterPinhole">OpenRegisterPinhole</a>" : <i>String</i>,
    "<a href="#openviapinhole" title="OpenViaPinhole">OpenViaPinhole</a>" : <i>String</i>,
    "<a href="#optionsrate" title="OptionsRate">OptionsRate</a>" : <i>Double</i>,
    "<a href="#prackrate" title="PrackRate">PrackRate</a>" : <i>Double</i>,
    "<a href="#preserveoverride" title="PreserveOverride">PreserveOverride</a>" : <i>String</i>,
    "<a href="#provisionalinviteexpirytime" title="ProvisionalInviteExpiryTime">ProvisionalInviteExpiryTime</a>" : <i>Double</i>,
    "<a href="#publishrate" title="PublishRate">PublishRate</a>" : <i>Double</i>,
    "<a href="#referrate" title="ReferRate">ReferRate</a>" : <i>Double</i>,
    "<a href="#registercontacttrace" title="RegisterContactTrace">RegisterContactTrace</a>" : <i>String</i>,
    "<a href="#registerrate" title="RegisterRate">RegisterRate</a>" : <i>Double</i>,
    "<a href="#rfc2543branch" title="Rfc2543Branch">Rfc2543Branch</a>" : <i>String</i>,
    "<a href="#rtp" title="Rtp">Rtp</a>" : <i>String</i>,
    "<a href="#sslalgorithm" title="SslAlgorithm">SslAlgorithm</a>" : <i>String</i>,
    "<a href="#sslauthclient" title="SslAuthClient">SslAuthClient</a>" : <i>String</i>,
    "<a href="#sslauthserver" title="SslAuthServer">SslAuthServer</a>" : <i>String</i>,
    "<a href="#sslclientcertificate" title="SslClientCertificate">SslClientCertificate</a>" : <i>String</i>,
    "<a href="#sslclientrenegotiation" title="SslClientRenegotiation">SslClientRenegotiation</a>" : <i>String</i>,
    "<a href="#sslmaxversion" title="SslMaxVersion">SslMaxVersion</a>" : <i>String</i>,
    "<a href="#sslminversion" title="SslMinVersion">SslMinVersion</a>" : <i>String</i>,
    "<a href="#sslmode" title="SslMode">SslMode</a>" : <i>String</i>,
    "<a href="#sslpfs" title="SslPfs">SslPfs</a>" : <i>String</i>,
    "<a href="#sslsendemptyfrags" title="SslSendEmptyFrags">SslSendEmptyFrags</a>" : <i>String</i>,
    "<a href="#sslservercertificate" title="SslServerCertificate">SslServerCertificate</a>" : <i>String</i>,
    "<a href="#status" title="Status">Status</a>" : <i>String</i>,
    "<a href="#strictregister" title="StrictRegister">StrictRegister</a>" : <i>String</i>,
    "<a href="#subscriberate" title="SubscribeRate">SubscribeRate</a>" : <i>Double</i>,
    "<a href="#unknownheader" title="UnknownHeader">UnknownHeader</a>" : <i>String</i>,
    "<a href="#updaterate" title="UpdateRate">UpdateRate</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#ackrate" title="AckRate">AckRate</a>: <i>Double</i>
<a href="#blockack" title="BlockAck">BlockAck</a>: <i>String</i>
<a href="#blockbye" title="BlockBye">BlockBye</a>: <i>String</i>
<a href="#blockcancel" title="BlockCancel">BlockCancel</a>: <i>String</i>
<a href="#blockgeoredoptions" title="BlockGeoRedOptions">BlockGeoRedOptions</a>: <i>String</i>
<a href="#blockinfo" title="BlockInfo">BlockInfo</a>: <i>String</i>
<a href="#blockinvite" title="BlockInvite">BlockInvite</a>: <i>String</i>
<a href="#blocklonglines" title="BlockLongLines">BlockLongLines</a>: <i>String</i>
<a href="#blockmessage" title="BlockMessage">BlockMessage</a>: <i>String</i>
<a href="#blocknotify" title="BlockNotify">BlockNotify</a>: <i>String</i>
<a href="#blockoptions" title="BlockOptions">BlockOptions</a>: <i>String</i>
<a href="#blockprack" title="BlockPrack">BlockPrack</a>: <i>String</i>
<a href="#blockpublish" title="BlockPublish">BlockPublish</a>: <i>String</i>
<a href="#blockrefer" title="BlockRefer">BlockRefer</a>: <i>String</i>
<a href="#blockregister" title="BlockRegister">BlockRegister</a>: <i>String</i>
<a href="#blocksubscribe" title="BlockSubscribe">BlockSubscribe</a>: <i>String</i>
<a href="#blockunknown" title="BlockUnknown">BlockUnknown</a>: <i>String</i>
<a href="#blockupdate" title="BlockUpdate">BlockUpdate</a>: <i>String</i>
<a href="#byerate" title="ByeRate">ByeRate</a>: <i>Double</i>
<a href="#callkeepalive" title="CallKeepalive">CallKeepalive</a>: <i>Double</i>
<a href="#cancelrate" title="CancelRate">CancelRate</a>: <i>Double</i>
<a href="#contactfixup" title="ContactFixup">ContactFixup</a>: <i>String</i>
<a href="#hntrestrictsourceip" title="HntRestrictSourceIp">HntRestrictSourceIp</a>: <i>String</i>
<a href="#hostednattraversal" title="HostedNatTraversal">HostedNatTraversal</a>: <i>String</i>
<a href="#inforate" title="InfoRate">InfoRate</a>: <i>Double</i>
<a href="#inviterate" title="InviteRate">InviteRate</a>: <i>Double</i>
<a href="#ipsrtp" title="IpsRtp">IpsRtp</a>: <i>String</i>
<a href="#logcallsummary" title="LogCallSummary">LogCallSummary</a>: <i>String</i>
<a href="#logviolations" title="LogViolations">LogViolations</a>: <i>String</i>
<a href="#malformedheaderallow" title="MalformedHeaderAllow">MalformedHeaderAllow</a>: <i>String</i>
<a href="#malformedheadercallid" title="MalformedHeaderCallId">MalformedHeaderCallId</a>: <i>String</i>
<a href="#malformedheadercontact" title="MalformedHeaderContact">MalformedHeaderContact</a>: <i>String</i>
<a href="#malformedheadercontentlength" title="MalformedHeaderContentLength">MalformedHeaderContentLength</a>: <i>String</i>
<a href="#malformedheadercontenttype" title="MalformedHeaderContentType">MalformedHeaderContentType</a>: <i>String</i>
<a href="#malformedheadercseq" title="MalformedHeaderCseq">MalformedHeaderCseq</a>: <i>String</i>
<a href="#malformedheaderexpires" title="MalformedHeaderExpires">MalformedHeaderExpires</a>: <i>String</i>
<a href="#malformedheaderfrom" title="MalformedHeaderFrom">MalformedHeaderFrom</a>: <i>String</i>
<a href="#malformedheadermaxforwards" title="MalformedHeaderMaxForwards">MalformedHeaderMaxForwards</a>: <i>String</i>
<a href="#malformedheaderpassertedidentity" title="MalformedHeaderPAssertedIdentity">MalformedHeaderPAssertedIdentity</a>: <i>String</i>
<a href="#malformedheaderrack" title="MalformedHeaderRack">MalformedHeaderRack</a>: <i>String</i>
<a href="#malformedheaderrecordroute" title="MalformedHeaderRecordRoute">MalformedHeaderRecordRoute</a>: <i>String</i>
<a href="#malformedheaderroute" title="MalformedHeaderRoute">MalformedHeaderRoute</a>: <i>String</i>
<a href="#malformedheaderrseq" title="MalformedHeaderRseq">MalformedHeaderRseq</a>: <i>String</i>
<a href="#malformedheadersdpa" title="MalformedHeaderSdpA">MalformedHeaderSdpA</a>: <i>String</i>
<a href="#malformedheadersdpb" title="MalformedHeaderSdpB">MalformedHeaderSdpB</a>: <i>String</i>
<a href="#malformedheadersdpc" title="MalformedHeaderSdpC">MalformedHeaderSdpC</a>: <i>String</i>
<a href="#malformedheadersdpi" title="MalformedHeaderSdpI">MalformedHeaderSdpI</a>: <i>String</i>
<a href="#malformedheadersdpk" title="MalformedHeaderSdpK">MalformedHeaderSdpK</a>: <i>String</i>
<a href="#malformedheadersdpm" title="MalformedHeaderSdpM">MalformedHeaderSdpM</a>: <i>String</i>
<a href="#malformedheadersdpo" title="MalformedHeaderSdpO">MalformedHeaderSdpO</a>: <i>String</i>
<a href="#malformedheadersdpr" title="MalformedHeaderSdpR">MalformedHeaderSdpR</a>: <i>String</i>
<a href="#malformedheadersdps" title="MalformedHeaderSdpS">MalformedHeaderSdpS</a>: <i>String</i>
<a href="#malformedheadersdpt" title="MalformedHeaderSdpT">MalformedHeaderSdpT</a>: <i>String</i>
<a href="#malformedheadersdpv" title="MalformedHeaderSdpV">MalformedHeaderSdpV</a>: <i>String</i>
<a href="#malformedheadersdpz" title="MalformedHeaderSdpZ">MalformedHeaderSdpZ</a>: <i>String</i>
<a href="#malformedheaderto" title="MalformedHeaderTo">MalformedHeaderTo</a>: <i>String</i>
<a href="#malformedheadervia" title="MalformedHeaderVia">MalformedHeaderVia</a>: <i>String</i>
<a href="#malformedrequestline" title="MalformedRequestLine">MalformedRequestLine</a>: <i>String</i>
<a href="#maxbodylength" title="MaxBodyLength">MaxBodyLength</a>: <i>Double</i>
<a href="#maxdialogs" title="MaxDialogs">MaxDialogs</a>: <i>Double</i>
<a href="#maxidledialogs" title="MaxIdleDialogs">MaxIdleDialogs</a>: <i>Double</i>
<a href="#maxlinelength" title="MaxLineLength">MaxLineLength</a>: <i>Double</i>
<a href="#messagerate" title="MessageRate">MessageRate</a>: <i>Double</i>
<a href="#natportrange" title="NatPortRange">NatPortRange</a>: <i>String</i>
<a href="#nattrace" title="NatTrace">NatTrace</a>: <i>String</i>
<a href="#nosdpfixup" title="NoSdpFixup">NoSdpFixup</a>: <i>String</i>
<a href="#notifyrate" title="NotifyRate">NotifyRate</a>: <i>Double</i>
<a href="#opencontactpinhole" title="OpenContactPinhole">OpenContactPinhole</a>: <i>String</i>
<a href="#openrecordroutepinhole" title="OpenRecordRoutePinhole">OpenRecordRoutePinhole</a>: <i>String</i>
<a href="#openregisterpinhole" title="OpenRegisterPinhole">OpenRegisterPinhole</a>: <i>String</i>
<a href="#openviapinhole" title="OpenViaPinhole">OpenViaPinhole</a>: <i>String</i>
<a href="#optionsrate" title="OptionsRate">OptionsRate</a>: <i>Double</i>
<a href="#prackrate" title="PrackRate">PrackRate</a>: <i>Double</i>
<a href="#preserveoverride" title="PreserveOverride">PreserveOverride</a>: <i>String</i>
<a href="#provisionalinviteexpirytime" title="ProvisionalInviteExpiryTime">ProvisionalInviteExpiryTime</a>: <i>Double</i>
<a href="#publishrate" title="PublishRate">PublishRate</a>: <i>Double</i>
<a href="#referrate" title="ReferRate">ReferRate</a>: <i>Double</i>
<a href="#registercontacttrace" title="RegisterContactTrace">RegisterContactTrace</a>: <i>String</i>
<a href="#registerrate" title="RegisterRate">RegisterRate</a>: <i>Double</i>
<a href="#rfc2543branch" title="Rfc2543Branch">Rfc2543Branch</a>: <i>String</i>
<a href="#rtp" title="Rtp">Rtp</a>: <i>String</i>
<a href="#sslalgorithm" title="SslAlgorithm">SslAlgorithm</a>: <i>String</i>
<a href="#sslauthclient" title="SslAuthClient">SslAuthClient</a>: <i>String</i>
<a href="#sslauthserver" title="SslAuthServer">SslAuthServer</a>: <i>String</i>
<a href="#sslclientcertificate" title="SslClientCertificate">SslClientCertificate</a>: <i>String</i>
<a href="#sslclientrenegotiation" title="SslClientRenegotiation">SslClientRenegotiation</a>: <i>String</i>
<a href="#sslmaxversion" title="SslMaxVersion">SslMaxVersion</a>: <i>String</i>
<a href="#sslminversion" title="SslMinVersion">SslMinVersion</a>: <i>String</i>
<a href="#sslmode" title="SslMode">SslMode</a>: <i>String</i>
<a href="#sslpfs" title="SslPfs">SslPfs</a>: <i>String</i>
<a href="#sslsendemptyfrags" title="SslSendEmptyFrags">SslSendEmptyFrags</a>: <i>String</i>
<a href="#sslservercertificate" title="SslServerCertificate">SslServerCertificate</a>: <i>String</i>
<a href="#status" title="Status">Status</a>: <i>String</i>
<a href="#strictregister" title="StrictRegister">StrictRegister</a>: <i>String</i>
<a href="#subscriberate" title="SubscribeRate">SubscribeRate</a>: <i>Double</i>
<a href="#unknownheader" title="UnknownHeader">UnknownHeader</a>: <i>String</i>
<a href="#updaterate" title="UpdateRate">UpdateRate</a>: <i>Double</i>
</pre>

## Properties

#### AckRate

ACK request rate limit (per second, per policy).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockAck

Enable/disable block ACK requests. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockBye

Enable/disable block BYE requests. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockCancel

Enable/disable block CANCEL requests. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockGeoRedOptions

Enable/disable block OPTIONS requests, but OPTIONS requests still notify for redundancy. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockInfo

Enable/disable block INFO requests. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockInvite

Enable/disable block INVITE requests. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockLongLines

Enable/disable block requests with headers exceeding max-line-length. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockMessage

Enable/disable block MESSAGE requests. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockNotify

Enable/disable block NOTIFY requests. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockOptions

Enable/disable block OPTIONS requests and no OPTIONS as notifying message for redundancy either. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockPrack

Enable/disable block prack requests. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockPublish

Enable/disable block PUBLISH requests. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockRefer

Enable/disable block REFER requests. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockRegister

Enable/disable block REGISTER requests. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockSubscribe

Enable/disable block SUBSCRIBE requests. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockUnknown

Block unrecognized SIP requests (enabled by default). Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockUpdate

Enable/disable block UPDATE requests. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ByeRate

BYE request rate limit (per second, per policy).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CallKeepalive

Continue tracking calls with no RTP for this many minutes.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CancelRate

CANCEL request rate limit (per second, per policy).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContactFixup

Fixup contact anyway even if contact's IP:port doesn't match session's IP:port. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HntRestrictSourceIp

Enable/disable restrict RTP source IP to be the same as SIP source IP when HNT is enabled. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostedNatTraversal

Hosted NAT Traversal (HNT). Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InfoRate

INFO request rate limit (per second, per policy).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InviteRate

INVITE request rate limit (per second, per policy).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsRtp

Enable/disable allow IPS on RTP. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogCallSummary

Enable/disable logging of SIP call summary. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogViolations

Enable/disable logging of SIP violations. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MalformedHeaderAllow

Action for malformed Allow header. Valid values: `discard`, `pass`, `respond`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MalformedHeaderCallId

Action for malformed Call-ID header. Valid values: `discard`, `pass`, `respond`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MalformedHeaderContact

Action for malformed Contact header. Valid values: `discard`, `pass`, `respond`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MalformedHeaderContentLength

Action for malformed Content-Length header. Valid values: `discard`, `pass`, `respond`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MalformedHeaderContentType

Action for malformed Content-Type header. Valid values: `discard`, `pass`, `respond`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MalformedHeaderCseq

Action for malformed CSeq header. Valid values: `discard`, `pass`, `respond`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MalformedHeaderExpires

Action for malformed Expires header. Valid values: `discard`, `pass`, `respond`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MalformedHeaderFrom

Action for malformed From header. Valid values: `discard`, `pass`, `respond`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MalformedHeaderMaxForwards

Action for malformed Max-Forwards header. Valid values: `discard`, `pass`, `respond`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MalformedHeaderPAssertedIdentity

Action for malformed P-Asserted-Identity header. Valid values: `discard`, `pass`, `respond`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MalformedHeaderRack

Action for malformed RAck header. Valid values: `discard`, `pass`, `respond`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MalformedHeaderRecordRoute

Action for malformed Record-Route header. Valid values: `discard`, `pass`, `respond`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MalformedHeaderRoute

Action for malformed Route header. Valid values: `discard`, `pass`, `respond`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MalformedHeaderRseq

Action for malformed RSeq header. Valid values: `discard`, `pass`, `respond`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MalformedHeaderSdpA

Action for malformed SDP a line. Valid values: `discard`, `pass`, `respond`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MalformedHeaderSdpB

Action for malformed SDP b line. Valid values: `discard`, `pass`, `respond`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MalformedHeaderSdpC

Action for malformed SDP c line. Valid values: `discard`, `pass`, `respond`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MalformedHeaderSdpI

Action for malformed SDP i line. Valid values: `discard`, `pass`, `respond`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MalformedHeaderSdpK

Action for malformed SDP k line. Valid values: `discard`, `pass`, `respond`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MalformedHeaderSdpM

Action for malformed SDP m line. Valid values: `discard`, `pass`, `respond`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MalformedHeaderSdpO

Action for malformed SDP o line. Valid values: `discard`, `pass`, `respond`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MalformedHeaderSdpR

Action for malformed SDP r line. Valid values: `discard`, `pass`, `respond`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MalformedHeaderSdpS

Action for malformed SDP s line. Valid values: `discard`, `pass`, `respond`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MalformedHeaderSdpT

Action for malformed SDP t line. Valid values: `discard`, `pass`, `respond`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MalformedHeaderSdpV

Action for malformed SDP v line. Valid values: `discard`, `pass`, `respond`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MalformedHeaderSdpZ

Action for malformed SDP z line. Valid values: `discard`, `pass`, `respond`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MalformedHeaderTo

Action for malformed To header. Valid values: `discard`, `pass`, `respond`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MalformedHeaderVia

Action for malformed VIA header. Valid values: `discard`, `pass`, `respond`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MalformedRequestLine

Action for malformed request line. Valid values: `discard`, `pass`, `respond`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxBodyLength

Maximum SIP message body length (0 meaning no limit).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxDialogs

Maximum number of concurrent calls/dialogs (per policy).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxIdleDialogs

Maximum number established but idle dialogs to retain (per policy).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxLineLength

Maximum SIP header line length (78-4096).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MessageRate

MESSAGE request rate limit (per second, per policy).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NatPortRange

RTP NAT port range.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NatTrace

Enable/disable preservation of original IP in SDP i line. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoSdpFixup

Enable/disable no SDP fix-up. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotifyRate

NOTIFY request rate limit (per second, per policy).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpenContactPinhole

Enable/disable open pinhole for non-REGISTER Contact port. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpenRecordRoutePinhole

Enable/disable open pinhole for Record-Route port. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpenRegisterPinhole

Enable/disable open pinhole for REGISTER Contact port. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpenViaPinhole

Enable/disable open pinhole for Via port. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OptionsRate

OPTIONS request rate limit (per second, per policy).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrackRate

PRACK request rate limit (per second, per policy).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreserveOverride

Override i line to preserve original IPS (default: append). Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProvisionalInviteExpiryTime

Expiry time for provisional INVITE (10 - 3600 sec).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublishRate

PUBLISH request rate limit (per second, per policy).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReferRate

REFER request rate limit (per second, per policy).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegisterContactTrace

Enable/disable trace original IP/port within the contact header of REGISTER requests. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegisterRate

REGISTER request rate limit (per second, per policy).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rfc2543Branch

Enable/disable support via branch compliant with RFC 2543. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rtp

Enable/disable create pinholes for RTP traffic to traverse firewall. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslAlgorithm

Relative strength of encryption algorithms accepted in negotiation. Valid values: `high`, `medium`, `low`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslAuthClient

Require a client certificate and authenticate it with the peer/peergrp.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslAuthServer

Authenticate the server's certificate with the peer/peergrp.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslClientCertificate

Name of Certificate to offer to server if requested.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslClientRenegotiation

Allow/block client renegotiation by server. Valid values: `allow`, `deny`, `secure`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslMaxVersion

Highest SSL/TLS version to negotiate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslMinVersion

Lowest SSL/TLS version to negotiate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslMode

SSL/TLS mode for encryption & decryption of traffic. Valid values: `off`, `full`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslPfs

SSL Perfect Forward Secrecy. Valid values: `require`, `deny`, `allow`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslSendEmptyFrags

Send empty fragments to avoid attack on CBC IV (SSL 3.0 & TLS 1.0 only). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslServerCertificate

Name of Certificate return to the client in every SSL connection.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable SIP. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StrictRegister

Enable/disable only allow the registrar to connect. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubscribeRate

SUBSCRIBE request rate limit (per second, per policy).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnknownHeader

Action for unknown SIP header. Valid values: `discard`, `pass`, `respond`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpdateRate

UPDATE request rate limit (per second, per policy).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

