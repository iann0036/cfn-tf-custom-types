# TF::Volterra::Fleet NetappBackendOntapNasDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#autoexportpolicy" title="AutoExportPolicy">AutoExportPolicy</a>" : <i>Boolean</i>,
    "<a href="#backendname" title="BackendName">BackendName</a>" : <i>String</i>,
    "<a href="#clientcertificate" title="ClientCertificate">ClientCertificate</a>" : <i>String</i>,
    "<a href="#datalifdnsname" title="DataLifDnsName">DataLifDnsName</a>" : <i>String</i>,
    "<a href="#datalifip" title="DataLifIp">DataLifIp</a>" : <i>String</i>,
    "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
    "<a href="#limitaggregateusage" title="LimitAggregateUsage">LimitAggregateUsage</a>" : <i>String</i>,
    "<a href="#limitvolumesize" title="LimitVolumeSize">LimitVolumeSize</a>" : <i>String</i>,
    "<a href="#managementlifdnsname" title="ManagementLifDnsName">ManagementLifDnsName</a>" : <i>String</i>,
    "<a href="#managementlifip" title="ManagementLifIp">ManagementLifIp</a>" : <i>String</i>,
    "<a href="#nfsmountoptions" title="NfsMountOptions">NfsMountOptions</a>" : <i>String</i>,
    "<a href="#region" title="Region">Region</a>" : <i>String</i>,
    "<a href="#storagedrivername" title="StorageDriverName">StorageDriverName</a>" : <i>String</i>,
    "<a href="#storageprefix" title="StoragePrefix">StoragePrefix</a>" : <i>String</i>,
    "<a href="#svm" title="Svm">Svm</a>" : <i>String</i>,
    "<a href="#trustedcacertificate" title="TrustedCaCertificate">TrustedCaCertificate</a>" : <i>String</i>,
    "<a href="#username" title="Username">Username</a>" : <i>String</i>,
    "<a href="#autoexportcidrs" title="AutoExportCidrs">AutoExportCidrs</a>" : <i>[ <a href="autoexportcidrsdefinition.md">AutoExportCidrsDefinition</a>, ... ]</i>,
    "<a href="#clientprivatekey" title="ClientPrivateKey">ClientPrivateKey</a>" : <i>[ <a href="clientprivatekeydefinition.md">ClientPrivateKeyDefinition</a>, ... ]</i>,
    "<a href="#password" title="Password">Password</a>" : <i>[ <a href="passworddefinition.md">PasswordDefinition</a>, ... ]</i>,
    "<a href="#storage" title="Storage">Storage</a>" : <i>[ <a href="storagedefinition.md">StorageDefinition</a>, ... ]</i>,
    "<a href="#volumedefaults" title="VolumeDefaults">VolumeDefaults</a>" : <i>[ <a href="volumedefaultsdefinition.md">VolumeDefaultsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#autoexportpolicy" title="AutoExportPolicy">AutoExportPolicy</a>: <i>Boolean</i>
<a href="#backendname" title="BackendName">BackendName</a>: <i>String</i>
<a href="#clientcertificate" title="ClientCertificate">ClientCertificate</a>: <i>String</i>
<a href="#datalifdnsname" title="DataLifDnsName">DataLifDnsName</a>: <i>String</i>
<a href="#datalifip" title="DataLifIp">DataLifIp</a>: <i>String</i>
<a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
<a href="#limitaggregateusage" title="LimitAggregateUsage">LimitAggregateUsage</a>: <i>String</i>
<a href="#limitvolumesize" title="LimitVolumeSize">LimitVolumeSize</a>: <i>String</i>
<a href="#managementlifdnsname" title="ManagementLifDnsName">ManagementLifDnsName</a>: <i>String</i>
<a href="#managementlifip" title="ManagementLifIp">ManagementLifIp</a>: <i>String</i>
<a href="#nfsmountoptions" title="NfsMountOptions">NfsMountOptions</a>: <i>String</i>
<a href="#region" title="Region">Region</a>: <i>String</i>
<a href="#storagedrivername" title="StorageDriverName">StorageDriverName</a>: <i>String</i>
<a href="#storageprefix" title="StoragePrefix">StoragePrefix</a>: <i>String</i>
<a href="#svm" title="Svm">Svm</a>: <i>String</i>
<a href="#trustedcacertificate" title="TrustedCaCertificate">TrustedCaCertificate</a>: <i>String</i>
<a href="#username" title="Username">Username</a>: <i>String</i>
<a href="#autoexportcidrs" title="AutoExportCidrs">AutoExportCidrs</a>: <i>
      - <a href="autoexportcidrsdefinition.md">AutoExportCidrsDefinition</a></i>
<a href="#clientprivatekey" title="ClientPrivateKey">ClientPrivateKey</a>: <i>
      - <a href="clientprivatekeydefinition.md">ClientPrivateKeyDefinition</a></i>
<a href="#password" title="Password">Password</a>: <i>
      - <a href="passworddefinition.md">PasswordDefinition</a></i>
<a href="#storage" title="Storage">Storage</a>: <i>
      - <a href="storagedefinition.md">StorageDefinition</a></i>
<a href="#volumedefaults" title="VolumeDefaults">VolumeDefaults</a>: <i>
      - <a href="volumedefaultsdefinition.md">VolumeDefaultsDefinition</a></i>
</pre>

## Properties

#### AutoExportPolicy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackendName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientCertificate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataLifDnsName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataLifIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LimitAggregateUsage

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LimitVolumeSize

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagementLifDnsName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagementLifIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NfsMountOptions

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageDriverName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StoragePrefix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Svm

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrustedCaCertificate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoExportCidrs

_Required_: No

_Type_: List of <a href="autoexportcidrsdefinition.md">AutoExportCidrsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientPrivateKey

_Required_: No

_Type_: List of <a href="clientprivatekeydefinition.md">ClientPrivateKeyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

_Required_: No

_Type_: List of <a href="passworddefinition.md">PasswordDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Storage

_Required_: No

_Type_: List of <a href="storagedefinition.md">StorageDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeDefaults

_Required_: No

_Type_: List of <a href="volumedefaultsdefinition.md">VolumeDefaultsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

