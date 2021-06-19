# TF::GoogleBeta::GoogleOsConfigGuestPolicies InstallStepsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#archiveextraction" title="ArchiveExtraction">ArchiveExtraction</a>" : <i>[ <a href="archiveextractiondefinition.md">ArchiveExtractionDefinition</a>, ... ]</i>,
    "<a href="#dpkginstallation" title="DpkgInstallation">DpkgInstallation</a>" : <i>[ <a href="dpkginstallationdefinition.md">DpkgInstallationDefinition</a>, ... ]</i>,
    "<a href="#filecopy" title="FileCopy">FileCopy</a>" : <i>[ <a href="filecopydefinition.md">FileCopyDefinition</a>, ... ]</i>,
    "<a href="#fileexec" title="FileExec">FileExec</a>" : <i>[ <a href="fileexecdefinition.md">FileExecDefinition</a>, ... ]</i>,
    "<a href="#msiinstallation" title="MsiInstallation">MsiInstallation</a>" : <i>[ <a href="msiinstallationdefinition.md">MsiInstallationDefinition</a>, ... ]</i>,
    "<a href="#rpminstallation" title="RpmInstallation">RpmInstallation</a>" : <i>[ <a href="rpminstallationdefinition.md">RpmInstallationDefinition</a>, ... ]</i>,
    "<a href="#scriptrun" title="ScriptRun">ScriptRun</a>" : <i>[ <a href="scriptrundefinition.md">ScriptRunDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#archiveextraction" title="ArchiveExtraction">ArchiveExtraction</a>: <i>
      - <a href="archiveextractiondefinition.md">ArchiveExtractionDefinition</a></i>
<a href="#dpkginstallation" title="DpkgInstallation">DpkgInstallation</a>: <i>
      - <a href="dpkginstallationdefinition.md">DpkgInstallationDefinition</a></i>
<a href="#filecopy" title="FileCopy">FileCopy</a>: <i>
      - <a href="filecopydefinition.md">FileCopyDefinition</a></i>
<a href="#fileexec" title="FileExec">FileExec</a>: <i>
      - <a href="fileexecdefinition.md">FileExecDefinition</a></i>
<a href="#msiinstallation" title="MsiInstallation">MsiInstallation</a>: <i>
      - <a href="msiinstallationdefinition.md">MsiInstallationDefinition</a></i>
<a href="#rpminstallation" title="RpmInstallation">RpmInstallation</a>: <i>
      - <a href="rpminstallationdefinition.md">RpmInstallationDefinition</a></i>
<a href="#scriptrun" title="ScriptRun">ScriptRun</a>: <i>
      - <a href="scriptrundefinition.md">ScriptRunDefinition</a></i>
</pre>

## Properties

#### ArchiveExtraction

_Required_: No

_Type_: List of <a href="archiveextractiondefinition.md">ArchiveExtractionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DpkgInstallation

_Required_: No

_Type_: List of <a href="dpkginstallationdefinition.md">DpkgInstallationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileCopy

_Required_: No

_Type_: List of <a href="filecopydefinition.md">FileCopyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileExec

_Required_: No

_Type_: List of <a href="fileexecdefinition.md">FileExecDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MsiInstallation

_Required_: No

_Type_: List of <a href="msiinstallationdefinition.md">MsiInstallationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RpmInstallation

_Required_: No

_Type_: List of <a href="rpminstallationdefinition.md">RpmInstallationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScriptRun

_Required_: No

_Type_: List of <a href="scriptrundefinition.md">ScriptRunDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

