# TF::Artifactory::RemoteRepository

CloudFormation equivalent of artifactory_remote_repository

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Artifactory::RemoteRepository",
    "Properties" : {
        "<a href="#allowanyhostauth" title="AllowAnyHostAuth">AllowAnyHostAuth</a>" : <i>Boolean</i>,
        "<a href="#blackedout" title="BlackedOut">BlackedOut</a>" : <i>Boolean</i>,
        "<a href="#blockmismatchingmimetypes" title="BlockMismatchingMimeTypes">BlockMismatchingMimeTypes</a>" : <i>Boolean</i>,
        "<a href="#bowerregistryurl" title="BowerRegistryUrl">BowerRegistryUrl</a>" : <i>String</i>,
        "<a href="#bypassheadrequests" title="BypassHeadRequests">BypassHeadRequests</a>" : <i>Boolean</i>,
        "<a href="#clienttlscertificate" title="ClientTlsCertificate">ClientTlsCertificate</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#downloadcontextpath" title="DownloadContextPath">DownloadContextPath</a>" : <i>String</i>,
        "<a href="#enablecookiemanagement" title="EnableCookieManagement">EnableCookieManagement</a>" : <i>Boolean</i>,
        "<a href="#enabletokenauthentication" title="EnableTokenAuthentication">EnableTokenAuthentication</a>" : <i>Boolean</i>,
        "<a href="#excludespattern" title="ExcludesPattern">ExcludesPattern</a>" : <i>String</i>,
        "<a href="#feedcontextpath" title="FeedContextPath">FeedContextPath</a>" : <i>String</i>,
        "<a href="#fetchjarseagerly" title="FetchJarsEagerly">FetchJarsEagerly</a>" : <i>Boolean</i>,
        "<a href="#fetchsourceseagerly" title="FetchSourcesEagerly">FetchSourcesEagerly</a>" : <i>Boolean</i>,
        "<a href="#forcenugetauthentication" title="ForceNugetAuthentication">ForceNugetAuthentication</a>" : <i>Boolean</i>,
        "<a href="#handlereleases" title="HandleReleases">HandleReleases</a>" : <i>Boolean</i>,
        "<a href="#handlesnapshots" title="HandleSnapshots">HandleSnapshots</a>" : <i>Boolean</i>,
        "<a href="#hardfail" title="HardFail">HardFail</a>" : <i>Boolean</i>,
        "<a href="#includespattern" title="IncludesPattern">IncludesPattern</a>" : <i>String</i>,
        "<a href="#key" title="Key">Key</a>" : <i>String</i>,
        "<a href="#localaddress" title="LocalAddress">LocalAddress</a>" : <i>String</i>,
        "<a href="#maxuniquesnapshots" title="MaxUniqueSnapshots">MaxUniqueSnapshots</a>" : <i>Double</i>,
        "<a href="#missedcacheperiodseconds" title="MissedCachePeriodSeconds">MissedCachePeriodSeconds</a>" : <i>Double</i>,
        "<a href="#notes" title="Notes">Notes</a>" : <i>String</i>,
        "<a href="#offline" title="Offline">Offline</a>" : <i>Boolean</i>,
        "<a href="#packagetype" title="PackageType">PackageType</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#propagatequeryparams" title="PropagateQueryParams">PropagateQueryParams</a>" : <i>Boolean</i>,
        "<a href="#propertysets" title="PropertySets">PropertySets</a>" : <i>[ String, ... ]</i>,
        "<a href="#proxy" title="Proxy">Proxy</a>" : <i>String</i>,
        "<a href="#pypiregistryurl" title="PypiRegistryUrl">PypiRegistryUrl</a>" : <i>String</i>,
        "<a href="#remoterepochecksumpolicytype" title="RemoteRepoChecksumPolicyType">RemoteRepoChecksumPolicyType</a>" : <i>String</i>,
        "<a href="#repolayoutref" title="RepoLayoutRef">RepoLayoutRef</a>" : <i>String</i>,
        "<a href="#retrievalcacheperiodseconds" title="RetrievalCachePeriodSeconds">RetrievalCachePeriodSeconds</a>" : <i>Double</i>,
        "<a href="#shareconfiguration" title="ShareConfiguration">ShareConfiguration</a>" : <i>Boolean</i>,
        "<a href="#sockettimeoutmillis" title="SocketTimeoutMillis">SocketTimeoutMillis</a>" : <i>Double</i>,
        "<a href="#storeartifactslocally" title="StoreArtifactsLocally">StoreArtifactsLocally</a>" : <i>Boolean</i>,
        "<a href="#suppresspomconsistencychecks" title="SuppressPomConsistencyChecks">SuppressPomConsistencyChecks</a>" : <i>Boolean</i>,
        "<a href="#synchronizeproperties" title="SynchronizeProperties">SynchronizeProperties</a>" : <i>Boolean</i>,
        "<a href="#unusedartifactscleanupperiodhours" title="UnusedArtifactsCleanupPeriodHours">UnusedArtifactsCleanupPeriodHours</a>" : <i>Double</i>,
        "<a href="#url" title="Url">Url</a>" : <i>String</i>,
        "<a href="#username" title="Username">Username</a>" : <i>String</i>,
        "<a href="#v3feedurl" title="V3FeedUrl">V3FeedUrl</a>" : <i>String</i>,
        "<a href="#vcsgitdownloadurl" title="VcsGitDownloadUrl">VcsGitDownloadUrl</a>" : <i>String</i>,
        "<a href="#vcsgitprovider" title="VcsGitProvider">VcsGitProvider</a>" : <i>String</i>,
        "<a href="#vcstype" title="VcsType">VcsType</a>" : <i>String</i>,
        "<a href="#xrayindex" title="XrayIndex">XrayIndex</a>" : <i>Boolean</i>,
        "<a href="#contentsynchronisation" title="ContentSynchronisation">ContentSynchronisation</a>" : <i>[ <a href="contentsynchronisationdefinition.md">ContentSynchronisationDefinition</a>, ... ]</i>,
        "<a href="#nuget" title="Nuget">Nuget</a>" : <i>[ <a href="nugetdefinition.md">NugetDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Artifactory::RemoteRepository
Properties:
    <a href="#allowanyhostauth" title="AllowAnyHostAuth">AllowAnyHostAuth</a>: <i>Boolean</i>
    <a href="#blackedout" title="BlackedOut">BlackedOut</a>: <i>Boolean</i>
    <a href="#blockmismatchingmimetypes" title="BlockMismatchingMimeTypes">BlockMismatchingMimeTypes</a>: <i>Boolean</i>
    <a href="#bowerregistryurl" title="BowerRegistryUrl">BowerRegistryUrl</a>: <i>String</i>
    <a href="#bypassheadrequests" title="BypassHeadRequests">BypassHeadRequests</a>: <i>Boolean</i>
    <a href="#clienttlscertificate" title="ClientTlsCertificate">ClientTlsCertificate</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#downloadcontextpath" title="DownloadContextPath">DownloadContextPath</a>: <i>String</i>
    <a href="#enablecookiemanagement" title="EnableCookieManagement">EnableCookieManagement</a>: <i>Boolean</i>
    <a href="#enabletokenauthentication" title="EnableTokenAuthentication">EnableTokenAuthentication</a>: <i>Boolean</i>
    <a href="#excludespattern" title="ExcludesPattern">ExcludesPattern</a>: <i>String</i>
    <a href="#feedcontextpath" title="FeedContextPath">FeedContextPath</a>: <i>String</i>
    <a href="#fetchjarseagerly" title="FetchJarsEagerly">FetchJarsEagerly</a>: <i>Boolean</i>
    <a href="#fetchsourceseagerly" title="FetchSourcesEagerly">FetchSourcesEagerly</a>: <i>Boolean</i>
    <a href="#forcenugetauthentication" title="ForceNugetAuthentication">ForceNugetAuthentication</a>: <i>Boolean</i>
    <a href="#handlereleases" title="HandleReleases">HandleReleases</a>: <i>Boolean</i>
    <a href="#handlesnapshots" title="HandleSnapshots">HandleSnapshots</a>: <i>Boolean</i>
    <a href="#hardfail" title="HardFail">HardFail</a>: <i>Boolean</i>
    <a href="#includespattern" title="IncludesPattern">IncludesPattern</a>: <i>String</i>
    <a href="#key" title="Key">Key</a>: <i>String</i>
    <a href="#localaddress" title="LocalAddress">LocalAddress</a>: <i>String</i>
    <a href="#maxuniquesnapshots" title="MaxUniqueSnapshots">MaxUniqueSnapshots</a>: <i>Double</i>
    <a href="#missedcacheperiodseconds" title="MissedCachePeriodSeconds">MissedCachePeriodSeconds</a>: <i>Double</i>
    <a href="#notes" title="Notes">Notes</a>: <i>String</i>
    <a href="#offline" title="Offline">Offline</a>: <i>Boolean</i>
    <a href="#packagetype" title="PackageType">PackageType</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#propagatequeryparams" title="PropagateQueryParams">PropagateQueryParams</a>: <i>Boolean</i>
    <a href="#propertysets" title="PropertySets">PropertySets</a>: <i>
      - String</i>
    <a href="#proxy" title="Proxy">Proxy</a>: <i>String</i>
    <a href="#pypiregistryurl" title="PypiRegistryUrl">PypiRegistryUrl</a>: <i>String</i>
    <a href="#remoterepochecksumpolicytype" title="RemoteRepoChecksumPolicyType">RemoteRepoChecksumPolicyType</a>: <i>String</i>
    <a href="#repolayoutref" title="RepoLayoutRef">RepoLayoutRef</a>: <i>String</i>
    <a href="#retrievalcacheperiodseconds" title="RetrievalCachePeriodSeconds">RetrievalCachePeriodSeconds</a>: <i>Double</i>
    <a href="#shareconfiguration" title="ShareConfiguration">ShareConfiguration</a>: <i>Boolean</i>
    <a href="#sockettimeoutmillis" title="SocketTimeoutMillis">SocketTimeoutMillis</a>: <i>Double</i>
    <a href="#storeartifactslocally" title="StoreArtifactsLocally">StoreArtifactsLocally</a>: <i>Boolean</i>
    <a href="#suppresspomconsistencychecks" title="SuppressPomConsistencyChecks">SuppressPomConsistencyChecks</a>: <i>Boolean</i>
    <a href="#synchronizeproperties" title="SynchronizeProperties">SynchronizeProperties</a>: <i>Boolean</i>
    <a href="#unusedartifactscleanupperiodhours" title="UnusedArtifactsCleanupPeriodHours">UnusedArtifactsCleanupPeriodHours</a>: <i>Double</i>
    <a href="#url" title="Url">Url</a>: <i>String</i>
    <a href="#username" title="Username">Username</a>: <i>String</i>
    <a href="#v3feedurl" title="V3FeedUrl">V3FeedUrl</a>: <i>String</i>
    <a href="#vcsgitdownloadurl" title="VcsGitDownloadUrl">VcsGitDownloadUrl</a>: <i>String</i>
    <a href="#vcsgitprovider" title="VcsGitProvider">VcsGitProvider</a>: <i>String</i>
    <a href="#vcstype" title="VcsType">VcsType</a>: <i>String</i>
    <a href="#xrayindex" title="XrayIndex">XrayIndex</a>: <i>Boolean</i>
    <a href="#contentsynchronisation" title="ContentSynchronisation">ContentSynchronisation</a>: <i>
      - <a href="contentsynchronisationdefinition.md">ContentSynchronisationDefinition</a></i>
    <a href="#nuget" title="Nuget">Nuget</a>: <i>
      - <a href="nugetdefinition.md">NugetDefinition</a></i>
</pre>

## Properties

#### AllowAnyHostAuth

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlackedOut

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockMismatchingMimeTypes

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BowerRegistryUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BypassHeadRequests

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientTlsCertificate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DownloadContextPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableCookieManagement

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableTokenAuthentication

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludesPattern

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FeedContextPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FetchJarsEagerly

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FetchSourcesEagerly

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceNugetAuthentication

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HandleReleases

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HandleSnapshots

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HardFail

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludesPattern

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Key

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxUniqueSnapshots

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MissedCachePeriodSeconds

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notes

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Offline

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PackageType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PropagateQueryParams

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PropertySets

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Proxy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PypiRegistryUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteRepoChecksumPolicyType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RepoLayoutRef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetrievalCachePeriodSeconds

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShareConfiguration

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SocketTimeoutMillis

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StoreArtifactsLocally

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SuppressPomConsistencyChecks

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SynchronizeProperties

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnusedArtifactsCleanupPeriodHours

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Url

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### V3FeedUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VcsGitDownloadUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VcsGitProvider

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VcsType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### XrayIndex

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentSynchronisation

_Required_: No

_Type_: List of <a href="contentsynchronisationdefinition.md">ContentSynchronisationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nuget

_Required_: No

_Type_: List of <a href="nugetdefinition.md">NugetDefinition</a>

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

