# TF::AVI::Systemconfiguration

The SystemConfiguration resource allows the creation and management of Avi SystemConfiguration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Systemconfiguration",
    "Properties" : {
        "<a href="#commoncriteriamode" title="CommonCriteriaMode">CommonCriteriaMode</a>" : <i>Boolean</i>,
        "<a href="#defaultlicensetier" title="DefaultLicenseTier">DefaultLicenseTier</a>" : <i>String</i>,
        "<a href="#dnsvirtualservicerefs" title="DnsVirtualserviceRefs">DnsVirtualserviceRefs</a>" : <i>[ String, ... ]</i>,
        "<a href="#dockermode" title="DockerMode">DockerMode</a>" : <i>Boolean</i>,
        "<a href="#enablecors" title="EnableCors">EnableCors</a>" : <i>Boolean</i>,
        "<a href="#fipsmode" title="FipsMode">FipsMode</a>" : <i>Boolean</i>,
        "<a href="#sshciphers" title="SshCiphers">SshCiphers</a>" : <i>[ String, ... ]</i>,
        "<a href="#sshhmacs" title="SshHmacs">SshHmacs</a>" : <i>[ String, ... ]</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#welcomeworkflowcomplete" title="WelcomeWorkflowComplete">WelcomeWorkflowComplete</a>" : <i>Boolean</i>,
        "<a href="#adminauthconfiguration" title="AdminAuthConfiguration">AdminAuthConfiguration</a>" : <i>[ <a href="adminauthconfigurationdefinition.md">AdminAuthConfigurationDefinition</a>, ... ]</i>,
        "<a href="#dnsconfiguration" title="DnsConfiguration">DnsConfiguration</a>" : <i>[ <a href="dnsconfigurationdefinition.md">DnsConfigurationDefinition</a>, ... ]</i>,
        "<a href="#emailconfiguration" title="EmailConfiguration">EmailConfiguration</a>" : <i>[ <a href="emailconfigurationdefinition.md">EmailConfigurationDefinition</a>, ... ]</i>,
        "<a href="#globaltenantconfig" title="GlobalTenantConfig">GlobalTenantConfig</a>" : <i>[ <a href="globaltenantconfigdefinition.md">GlobalTenantConfigDefinition</a>, ... ]</i>,
        "<a href="#linuxconfiguration" title="LinuxConfiguration">LinuxConfiguration</a>" : <i>[ <a href="linuxconfigurationdefinition.md">LinuxConfigurationDefinition</a>, ... ]</i>,
        "<a href="#mgmtipaccesscontrol" title="MgmtIpAccessControl">MgmtIpAccessControl</a>" : <i>[ <a href="mgmtipaccesscontroldefinition.md">MgmtIpAccessControlDefinition</a>, ... ]</i>,
        "<a href="#ntpconfiguration" title="NtpConfiguration">NtpConfiguration</a>" : <i>[ <a href="ntpconfigurationdefinition.md">NtpConfigurationDefinition</a>, ... ]</i>,
        "<a href="#portalconfiguration" title="PortalConfiguration">PortalConfiguration</a>" : <i>[ <a href="portalconfigurationdefinition.md">PortalConfigurationDefinition</a>, ... ]</i>,
        "<a href="#proxyconfiguration" title="ProxyConfiguration">ProxyConfiguration</a>" : <i>[ <a href="proxyconfigurationdefinition.md">ProxyConfigurationDefinition</a>, ... ]</i>,
        "<a href="#securechannelconfiguration" title="SecureChannelConfiguration">SecureChannelConfiguration</a>" : <i>[ <a href="securechannelconfigurationdefinition.md">SecureChannelConfigurationDefinition</a>, ... ]</i>,
        "<a href="#snmpconfiguration" title="SnmpConfiguration">SnmpConfiguration</a>" : <i>[ <a href="snmpconfigurationdefinition.md">SnmpConfigurationDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Systemconfiguration
Properties:
    <a href="#commoncriteriamode" title="CommonCriteriaMode">CommonCriteriaMode</a>: <i>Boolean</i>
    <a href="#defaultlicensetier" title="DefaultLicenseTier">DefaultLicenseTier</a>: <i>String</i>
    <a href="#dnsvirtualservicerefs" title="DnsVirtualserviceRefs">DnsVirtualserviceRefs</a>: <i>
      - String</i>
    <a href="#dockermode" title="DockerMode">DockerMode</a>: <i>Boolean</i>
    <a href="#enablecors" title="EnableCors">EnableCors</a>: <i>Boolean</i>
    <a href="#fipsmode" title="FipsMode">FipsMode</a>: <i>Boolean</i>
    <a href="#sshciphers" title="SshCiphers">SshCiphers</a>: <i>
      - String</i>
    <a href="#sshhmacs" title="SshHmacs">SshHmacs</a>: <i>
      - String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#welcomeworkflowcomplete" title="WelcomeWorkflowComplete">WelcomeWorkflowComplete</a>: <i>Boolean</i>
    <a href="#adminauthconfiguration" title="AdminAuthConfiguration">AdminAuthConfiguration</a>: <i>
      - <a href="adminauthconfigurationdefinition.md">AdminAuthConfigurationDefinition</a></i>
    <a href="#dnsconfiguration" title="DnsConfiguration">DnsConfiguration</a>: <i>
      - <a href="dnsconfigurationdefinition.md">DnsConfigurationDefinition</a></i>
    <a href="#emailconfiguration" title="EmailConfiguration">EmailConfiguration</a>: <i>
      - <a href="emailconfigurationdefinition.md">EmailConfigurationDefinition</a></i>
    <a href="#globaltenantconfig" title="GlobalTenantConfig">GlobalTenantConfig</a>: <i>
      - <a href="globaltenantconfigdefinition.md">GlobalTenantConfigDefinition</a></i>
    <a href="#linuxconfiguration" title="LinuxConfiguration">LinuxConfiguration</a>: <i>
      - <a href="linuxconfigurationdefinition.md">LinuxConfigurationDefinition</a></i>
    <a href="#mgmtipaccesscontrol" title="MgmtIpAccessControl">MgmtIpAccessControl</a>: <i>
      - <a href="mgmtipaccesscontroldefinition.md">MgmtIpAccessControlDefinition</a></i>
    <a href="#ntpconfiguration" title="NtpConfiguration">NtpConfiguration</a>: <i>
      - <a href="ntpconfigurationdefinition.md">NtpConfigurationDefinition</a></i>
    <a href="#portalconfiguration" title="PortalConfiguration">PortalConfiguration</a>: <i>
      - <a href="portalconfigurationdefinition.md">PortalConfigurationDefinition</a></i>
    <a href="#proxyconfiguration" title="ProxyConfiguration">ProxyConfiguration</a>: <i>
      - <a href="proxyconfigurationdefinition.md">ProxyConfigurationDefinition</a></i>
    <a href="#securechannelconfiguration" title="SecureChannelConfiguration">SecureChannelConfiguration</a>: <i>
      - <a href="securechannelconfigurationdefinition.md">SecureChannelConfigurationDefinition</a></i>
    <a href="#snmpconfiguration" title="SnmpConfiguration">SnmpConfiguration</a>: <i>
      - <a href="snmpconfigurationdefinition.md">SnmpConfigurationDefinition</a></i>
</pre>

## Properties

#### CommonCriteriaMode

Common criteria mode's current state. Field introduced in 20.1.3.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultLicenseTier

Specifies the default license tier which would be used by new clouds. Enum options - ENTERPRISE_16, ENTERPRISE, ENTERPRISE_18, BASIC, ESSENTIALS. Field introduced in 17.2.5. Allowed in basic edition, essentials edition, enterprise edition. Special default for basic edition is basic, essentials edition is essentials, enterprise is enterprise.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsVirtualserviceRefs

Dns virtualservices hosting fqdn records for applications across avi vantage. If no virtualservices are provided, avi vantage will provide dns services for configured applications. Switching back to avi vantage from dns virtualservices is not allowed. It is a reference to an object of type virtualservice.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DockerMode

Boolean flag to set docker_mode.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableCors

Enable cors header. Field introduced in 20.1.3. Allowed in basic edition, essentials edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FipsMode

Fips mode current state. Field introduced in 20.1.1.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshCiphers

Allowed ciphers list for ssh to the management interface on the controller and service engines. If this is not specified, all the default ciphers are allowed.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshHmacs

Allowed hmac list for ssh to the management interface on the controller and service engines. If this is not specified, all the default hmacs are allowed.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WelcomeWorkflowComplete

This flag is set once the initial controller setup workflow is complete. Field introduced in 18.2.3.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminAuthConfiguration

_Required_: No

_Type_: List of <a href="adminauthconfigurationdefinition.md">AdminAuthConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsConfiguration

_Required_: No

_Type_: List of <a href="dnsconfigurationdefinition.md">DnsConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailConfiguration

_Required_: No

_Type_: List of <a href="emailconfigurationdefinition.md">EmailConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GlobalTenantConfig

_Required_: No

_Type_: List of <a href="globaltenantconfigdefinition.md">GlobalTenantConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LinuxConfiguration

_Required_: No

_Type_: List of <a href="linuxconfigurationdefinition.md">LinuxConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MgmtIpAccessControl

_Required_: No

_Type_: List of <a href="mgmtipaccesscontroldefinition.md">MgmtIpAccessControlDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NtpConfiguration

_Required_: No

_Type_: List of <a href="ntpconfigurationdefinition.md">NtpConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortalConfiguration

_Required_: No

_Type_: List of <a href="portalconfigurationdefinition.md">PortalConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyConfiguration

_Required_: No

_Type_: List of <a href="proxyconfigurationdefinition.md">ProxyConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecureChannelConfiguration

_Required_: No

_Type_: List of <a href="securechannelconfigurationdefinition.md">SecureChannelConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnmpConfiguration

_Required_: No

_Type_: List of <a href="snmpconfigurationdefinition.md">SnmpConfigurationDefinition</a>

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

