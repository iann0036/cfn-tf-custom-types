# TF::Aviatrix::Gateway

The **aviatrix_gateway** resource allows the creation and management of Aviatrix gateways.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aviatrix::Gateway",
    "Properties" : {
        "<a href="#accountname" title="AccountName">AccountName</a>" : <i>String</i>,
        "<a href="#additionalcidrs" title="AdditionalCidrs">AdditionalCidrs</a>" : <i>String</i>,
        "<a href="#additionalcidrsdesignatedgateway" title="AdditionalCidrsDesignatedGateway">AdditionalCidrsDesignatedGateway</a>" : <i>String</i>,
        "<a href="#allocateneweip" title="AllocateNewEip">AllocateNewEip</a>" : <i>Boolean</i>,
        "<a href="#availabilitydomain" title="AvailabilityDomain">AvailabilityDomain</a>" : <i>String</i>,
        "<a href="#cloudtype" title="CloudType">CloudType</a>" : <i>Double</i>,
        "<a href="#customermanagedkeys" title="CustomerManagedKeys">CustomerManagedKeys</a>" : <i>String</i>,
        "<a href="#duoapihostname" title="DuoApiHostname">DuoApiHostname</a>" : <i>String</i>,
        "<a href="#duointegrationkey" title="DuoIntegrationKey">DuoIntegrationKey</a>" : <i>String</i>,
        "<a href="#duopushmode" title="DuoPushMode">DuoPushMode</a>" : <i>String</i>,
        "<a href="#duosecretkey" title="DuoSecretKey">DuoSecretKey</a>" : <i>String</i>,
        "<a href="#eip" title="Eip">Eip</a>" : <i>String</i>,
        "<a href="#elbname" title="ElbName">ElbName</a>" : <i>String</i>,
        "<a href="#enabledesignatedgateway" title="EnableDesignatedGateway">EnableDesignatedGateway</a>" : <i>Boolean</i>,
        "<a href="#enableelb" title="EnableElb">EnableElb</a>" : <i>Boolean</i>,
        "<a href="#enableencryptvolume" title="EnableEncryptVolume">EnableEncryptVolume</a>" : <i>Boolean</i>,
        "<a href="#enablejumboframe" title="EnableJumboFrame">EnableJumboFrame</a>" : <i>Boolean</i>,
        "<a href="#enableldap" title="EnableLdap">EnableLdap</a>" : <i>Boolean</i>,
        "<a href="#enablemonitorgatewaysubnets" title="EnableMonitorGatewaySubnets">EnableMonitorGatewaySubnets</a>" : <i>Boolean</i>,
        "<a href="#enablepublicsubnetfiltering" title="EnablePublicSubnetFiltering">EnablePublicSubnetFiltering</a>" : <i>Boolean</i>,
        "<a href="#enablevpcdnsserver" title="EnableVpcDnsServer">EnableVpcDnsServer</a>" : <i>Boolean</i>,
        "<a href="#enablevpnnat" title="EnableVpnNat">EnableVpnNat</a>" : <i>Boolean</i>,
        "<a href="#faultdomain" title="FaultDomain">FaultDomain</a>" : <i>String</i>,
        "<a href="#fqdnlancidr" title="FqdnLanCidr">FqdnLanCidr</a>" : <i>String</i>,
        "<a href="#fqdnlanvpcid" title="FqdnLanVpcId">FqdnLanVpcId</a>" : <i>String</i>,
        "<a href="#gwname" title="GwName">GwName</a>" : <i>String</i>,
        "<a href="#gwsize" title="GwSize">GwSize</a>" : <i>String</i>,
        "<a href="#idletimeout" title="IdleTimeout">IdleTimeout</a>" : <i>Double</i>,
        "<a href="#insanemode" title="InsaneMode">InsaneMode</a>" : <i>Boolean</i>,
        "<a href="#insanemodeaz" title="InsaneModeAz">InsaneModeAz</a>" : <i>String</i>,
        "<a href="#ldapbasedn" title="LdapBaseDn">LdapBaseDn</a>" : <i>String</i>,
        "<a href="#ldapbinddn" title="LdapBindDn">LdapBindDn</a>" : <i>String</i>,
        "<a href="#ldappassword" title="LdapPassword">LdapPassword</a>" : <i>String</i>,
        "<a href="#ldapserver" title="LdapServer">LdapServer</a>" : <i>String</i>,
        "<a href="#ldapusernameattribute" title="LdapUsernameAttribute">LdapUsernameAttribute</a>" : <i>String</i>,
        "<a href="#maxvpnconn" title="MaxVpnConn">MaxVpnConn</a>" : <i>String</i>,
        "<a href="#monitorexcludelist" title="MonitorExcludeList">MonitorExcludeList</a>" : <i>[ String, ... ]</i>,
        "<a href="#nameservers" title="NameServers">NameServers</a>" : <i>String</i>,
        "<a href="#oktatoken" title="OktaToken">OktaToken</a>" : <i>String</i>,
        "<a href="#oktaurl" title="OktaUrl">OktaUrl</a>" : <i>String</i>,
        "<a href="#oktausernamesuffix" title="OktaUsernameSuffix">OktaUsernameSuffix</a>" : <i>String</i>,
        "<a href="#otpmode" title="OtpMode">OtpMode</a>" : <i>String</i>,
        "<a href="#peeringhaavailabilitydomain" title="PeeringHaAvailabilityDomain">PeeringHaAvailabilityDomain</a>" : <i>String</i>,
        "<a href="#peeringhaeip" title="PeeringHaEip">PeeringHaEip</a>" : <i>String</i>,
        "<a href="#peeringhafaultdomain" title="PeeringHaFaultDomain">PeeringHaFaultDomain</a>" : <i>String</i>,
        "<a href="#peeringhagwsize" title="PeeringHaGwSize">PeeringHaGwSize</a>" : <i>String</i>,
        "<a href="#peeringhainsanemodeaz" title="PeeringHaInsaneModeAz">PeeringHaInsaneModeAz</a>" : <i>String</i>,
        "<a href="#peeringhasubnet" title="PeeringHaSubnet">PeeringHaSubnet</a>" : <i>String</i>,
        "<a href="#peeringhazone" title="PeeringHaZone">PeeringHaZone</a>" : <i>String</i>,
        "<a href="#publicsubnetfilteringguarddutyenforced" title="PublicSubnetFilteringGuardDutyEnforced">PublicSubnetFilteringGuardDutyEnforced</a>" : <i>Boolean</i>,
        "<a href="#publicsubnetfilteringharoutetables" title="PublicSubnetFilteringHaRouteTables">PublicSubnetFilteringHaRouteTables</a>" : <i>[ String, ... ]</i>,
        "<a href="#publicsubnetfilteringroutetables" title="PublicSubnetFilteringRouteTables">PublicSubnetFilteringRouteTables</a>" : <i>[ String, ... ]</i>,
        "<a href="#renegotiationinterval" title="RenegotiationInterval">RenegotiationInterval</a>" : <i>Double</i>,
        "<a href="#samlenabled" title="SamlEnabled">SamlEnabled</a>" : <i>Boolean</i>,
        "<a href="#searchdomains" title="SearchDomains">SearchDomains</a>" : <i>String</i>,
        "<a href="#singleazha" title="SingleAzHa">SingleAzHa</a>" : <i>Boolean</i>,
        "<a href="#singleipsnat" title="SingleIpSnat">SingleIpSnat</a>" : <i>Boolean</i>,
        "<a href="#splittunnel" title="SplitTunnel">SplitTunnel</a>" : <i>Boolean</i>,
        "<a href="#storagename" title="StorageName">StorageName</a>" : <i>String</i>,
        "<a href="#subnet" title="Subnet">Subnet</a>" : <i>String</i>,
        "<a href="#taglist" title="TagList">TagList</a>" : <i>[ String, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tunneldetectiontime" title="TunnelDetectionTime">TunnelDetectionTime</a>" : <i>Double</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#vpcreg" title="VpcReg">VpcReg</a>" : <i>String</i>,
        "<a href="#vpnaccess" title="VpnAccess">VpnAccess</a>" : <i>Boolean</i>,
        "<a href="#vpncidr" title="VpnCidr">VpnCidr</a>" : <i>String</i>,
        "<a href="#vpnprotocol" title="VpnProtocol">VpnProtocol</a>" : <i>String</i>,
        "<a href="#zone" title="Zone">Zone</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Aviatrix::Gateway
Properties:
    <a href="#accountname" title="AccountName">AccountName</a>: <i>String</i>
    <a href="#additionalcidrs" title="AdditionalCidrs">AdditionalCidrs</a>: <i>String</i>
    <a href="#additionalcidrsdesignatedgateway" title="AdditionalCidrsDesignatedGateway">AdditionalCidrsDesignatedGateway</a>: <i>String</i>
    <a href="#allocateneweip" title="AllocateNewEip">AllocateNewEip</a>: <i>Boolean</i>
    <a href="#availabilitydomain" title="AvailabilityDomain">AvailabilityDomain</a>: <i>String</i>
    <a href="#cloudtype" title="CloudType">CloudType</a>: <i>Double</i>
    <a href="#customermanagedkeys" title="CustomerManagedKeys">CustomerManagedKeys</a>: <i>String</i>
    <a href="#duoapihostname" title="DuoApiHostname">DuoApiHostname</a>: <i>String</i>
    <a href="#duointegrationkey" title="DuoIntegrationKey">DuoIntegrationKey</a>: <i>String</i>
    <a href="#duopushmode" title="DuoPushMode">DuoPushMode</a>: <i>String</i>
    <a href="#duosecretkey" title="DuoSecretKey">DuoSecretKey</a>: <i>String</i>
    <a href="#eip" title="Eip">Eip</a>: <i>String</i>
    <a href="#elbname" title="ElbName">ElbName</a>: <i>String</i>
    <a href="#enabledesignatedgateway" title="EnableDesignatedGateway">EnableDesignatedGateway</a>: <i>Boolean</i>
    <a href="#enableelb" title="EnableElb">EnableElb</a>: <i>Boolean</i>
    <a href="#enableencryptvolume" title="EnableEncryptVolume">EnableEncryptVolume</a>: <i>Boolean</i>
    <a href="#enablejumboframe" title="EnableJumboFrame">EnableJumboFrame</a>: <i>Boolean</i>
    <a href="#enableldap" title="EnableLdap">EnableLdap</a>: <i>Boolean</i>
    <a href="#enablemonitorgatewaysubnets" title="EnableMonitorGatewaySubnets">EnableMonitorGatewaySubnets</a>: <i>Boolean</i>
    <a href="#enablepublicsubnetfiltering" title="EnablePublicSubnetFiltering">EnablePublicSubnetFiltering</a>: <i>Boolean</i>
    <a href="#enablevpcdnsserver" title="EnableVpcDnsServer">EnableVpcDnsServer</a>: <i>Boolean</i>
    <a href="#enablevpnnat" title="EnableVpnNat">EnableVpnNat</a>: <i>Boolean</i>
    <a href="#faultdomain" title="FaultDomain">FaultDomain</a>: <i>String</i>
    <a href="#fqdnlancidr" title="FqdnLanCidr">FqdnLanCidr</a>: <i>String</i>
    <a href="#fqdnlanvpcid" title="FqdnLanVpcId">FqdnLanVpcId</a>: <i>String</i>
    <a href="#gwname" title="GwName">GwName</a>: <i>String</i>
    <a href="#gwsize" title="GwSize">GwSize</a>: <i>String</i>
    <a href="#idletimeout" title="IdleTimeout">IdleTimeout</a>: <i>Double</i>
    <a href="#insanemode" title="InsaneMode">InsaneMode</a>: <i>Boolean</i>
    <a href="#insanemodeaz" title="InsaneModeAz">InsaneModeAz</a>: <i>String</i>
    <a href="#ldapbasedn" title="LdapBaseDn">LdapBaseDn</a>: <i>String</i>
    <a href="#ldapbinddn" title="LdapBindDn">LdapBindDn</a>: <i>String</i>
    <a href="#ldappassword" title="LdapPassword">LdapPassword</a>: <i>String</i>
    <a href="#ldapserver" title="LdapServer">LdapServer</a>: <i>String</i>
    <a href="#ldapusernameattribute" title="LdapUsernameAttribute">LdapUsernameAttribute</a>: <i>String</i>
    <a href="#maxvpnconn" title="MaxVpnConn">MaxVpnConn</a>: <i>String</i>
    <a href="#monitorexcludelist" title="MonitorExcludeList">MonitorExcludeList</a>: <i>
      - String</i>
    <a href="#nameservers" title="NameServers">NameServers</a>: <i>String</i>
    <a href="#oktatoken" title="OktaToken">OktaToken</a>: <i>String</i>
    <a href="#oktaurl" title="OktaUrl">OktaUrl</a>: <i>String</i>
    <a href="#oktausernamesuffix" title="OktaUsernameSuffix">OktaUsernameSuffix</a>: <i>String</i>
    <a href="#otpmode" title="OtpMode">OtpMode</a>: <i>String</i>
    <a href="#peeringhaavailabilitydomain" title="PeeringHaAvailabilityDomain">PeeringHaAvailabilityDomain</a>: <i>String</i>
    <a href="#peeringhaeip" title="PeeringHaEip">PeeringHaEip</a>: <i>String</i>
    <a href="#peeringhafaultdomain" title="PeeringHaFaultDomain">PeeringHaFaultDomain</a>: <i>String</i>
    <a href="#peeringhagwsize" title="PeeringHaGwSize">PeeringHaGwSize</a>: <i>String</i>
    <a href="#peeringhainsanemodeaz" title="PeeringHaInsaneModeAz">PeeringHaInsaneModeAz</a>: <i>String</i>
    <a href="#peeringhasubnet" title="PeeringHaSubnet">PeeringHaSubnet</a>: <i>String</i>
    <a href="#peeringhazone" title="PeeringHaZone">PeeringHaZone</a>: <i>String</i>
    <a href="#publicsubnetfilteringguarddutyenforced" title="PublicSubnetFilteringGuardDutyEnforced">PublicSubnetFilteringGuardDutyEnforced</a>: <i>Boolean</i>
    <a href="#publicsubnetfilteringharoutetables" title="PublicSubnetFilteringHaRouteTables">PublicSubnetFilteringHaRouteTables</a>: <i>
      - String</i>
    <a href="#publicsubnetfilteringroutetables" title="PublicSubnetFilteringRouteTables">PublicSubnetFilteringRouteTables</a>: <i>
      - String</i>
    <a href="#renegotiationinterval" title="RenegotiationInterval">RenegotiationInterval</a>: <i>Double</i>
    <a href="#samlenabled" title="SamlEnabled">SamlEnabled</a>: <i>Boolean</i>
    <a href="#searchdomains" title="SearchDomains">SearchDomains</a>: <i>String</i>
    <a href="#singleazha" title="SingleAzHa">SingleAzHa</a>: <i>Boolean</i>
    <a href="#singleipsnat" title="SingleIpSnat">SingleIpSnat</a>: <i>Boolean</i>
    <a href="#splittunnel" title="SplitTunnel">SplitTunnel</a>: <i>Boolean</i>
    <a href="#storagename" title="StorageName">StorageName</a>: <i>String</i>
    <a href="#subnet" title="Subnet">Subnet</a>: <i>String</i>
    <a href="#taglist" title="TagList">TagList</a>: <i>
      - String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tunneldetectiontime" title="TunnelDetectionTime">TunnelDetectionTime</a>: <i>Double</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#vpcreg" title="VpcReg">VpcReg</a>: <i>String</i>
    <a href="#vpnaccess" title="VpnAccess">VpnAccess</a>: <i>Boolean</i>
    <a href="#vpncidr" title="VpnCidr">VpnCidr</a>: <i>String</i>
    <a href="#vpnprotocol" title="VpnProtocol">VpnProtocol</a>: <i>String</i>
    <a href="#zone" title="Zone">Zone</a>: <i>String</i>
</pre>

## Properties

#### AccountName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdditionalCidrs

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdditionalCidrsDesignatedGateway

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllocateNewEip

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailabilityDomain

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudType

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomerManagedKeys

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DuoApiHostname

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DuoIntegrationKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DuoPushMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DuoSecretKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Eip

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ElbName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableDesignatedGateway

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableElb

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableEncryptVolume

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableJumboFrame

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableLdap

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableMonitorGatewaySubnets

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnablePublicSubnetFiltering

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableVpcDnsServer

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableVpnNat

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FaultDomain

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FqdnLanCidr

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FqdnLanVpcId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GwName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GwSize

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdleTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsaneMode

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsaneModeAz

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LdapBaseDn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LdapBindDn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LdapPassword

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LdapServer

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LdapUsernameAttribute

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxVpnConn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MonitorExcludeList

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameServers

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OktaToken

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OktaUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OktaUsernameSuffix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OtpMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeeringHaAvailabilityDomain

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeeringHaEip

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeeringHaFaultDomain

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeeringHaGwSize

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeeringHaInsaneModeAz

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeeringHaSubnet

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeeringHaZone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicSubnetFilteringGuardDutyEnforced

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicSubnetFilteringHaRouteTables

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicSubnetFilteringRouteTables

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RenegotiationInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SamlEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SearchDomains

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SingleAzHa

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SingleIpSnat

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SplitTunnel

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnet

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagList

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TunnelDetectionTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcReg

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpnAccess

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpnCidr

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpnProtocol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CloudInstanceId

Returns the <code>CloudInstanceId</code> value.

#### ElbDnsName

Returns the <code>ElbDnsName</code> value.

#### FqdnLanInterface

Returns the <code>FqdnLanInterface</code> value.

#### Id

Returns the <code>Id</code> value.

#### PeeringHaCloudInstanceId

Returns the <code>PeeringHaCloudInstanceId</code> value.

#### PeeringHaGwName

Returns the <code>PeeringHaGwName</code> value.

#### PeeringHaPrivateIp

Returns the <code>PeeringHaPrivateIp</code> value.

#### PrivateIp

Returns the <code>PrivateIp</code> value.

#### PublicDnsServer

Returns the <code>PublicDnsServer</code> value.

#### SecurityGroupId

Returns the <code>SecurityGroupId</code> value.

